import pathlib
import openfe

from rdkit import Chem
from openfe import LigandNetwork, LigandAtomMapping
# from openfe.setup.ligand_network_planning import load_orion_network
from openfe.setup.atom_mapping import LomapAtomMapper, KartografAtomMapper
from openfe.protocols.openmm_rfe import RelativeHybridTopologyProtocol
from openfe.protocols.openmm_utils.omm_settings import OpenFFPartialChargeSettings
from openfe.protocols.openmm_utils.charge_generation import bulk_assign_partial_charges
from openff.units import unit

from concurrent.futures import ProcessPoolExecutor


def map_single_edge(ligand_a, ligand_b, mapper):
    # Generates a generator of mappings; we take the best (first) one
    mappings = list(mapper.suggest_mappings(ligand_a, ligand_b))
    return mappings[0] if mappings else None


def load_custom_network_parallel(ligands: list, mapper, network_file: str, max_workers: int = 16):
    # Create a lookup dictionary for molecules by their names
    ligand_dict = {lig.name: lig for lig in ligands}
    edges_to_map = []

    # 2. Parse the network file to extract the pairs
    with open(network_file, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            # Adjust the split logic depending on your Orion NES file structure
            name_a, _doublearrow, name_b = line.strip().split()[:3]
            if name_a in ligand_dict and name_b in ligand_dict:
                edges_to_map.append((ligand_dict[name_a], ligand_dict[name_b]))

    # 3. Map pairs concurrently across multiple processors
    completed_mappings = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit mapping tasks
        futures = [
            executor.submit(map_single_edge, lig_a, lig_b, mapper)
            for lig_a, lig_b in edges_to_map
        ]
        
        for future in futures:
            mapping = future.result()
            if mapping:
                completed_mappings.append(mapping)

    # 4. Construct and return the final OpenFE LigandNetwork
    return LigandNetwork(edges=completed_mappings, nodes=ligands)


charge_settings = OpenFFPartialChargeSettings(
        partial_charge_method="nagl", # "am1bcc", 
        off_toolkit_backend="ambertools"
        )

settings = RelativeHybridTopologyProtocol.default_settings()
#settings.thermo_settings.temperature  # ex. display default value (298.15 kelvin)
# change the value
#settings.thermo_settings.temperature = 310.0 * unit.kelvin
# defaults are water with NaCl at 0.15 M
solvent = openfe.SolventComponent()
# Create a protocol for the solvent legs using default settings
solvent_protocol = RelativeHybridTopologyProtocol(RelativeHybridTopologyProtocol.default_settings())
# Create a prrotocol for the complex legs with a reduced solvent padding
complex_settings = RelativeHybridTopologyProtocol.default_settings()
complex_settings.solvation_settings.solvent_padding = 1 * unit.nanometer
complex_protocol = RelativeHybridTopologyProtocol(complex_settings)


workdir = pathlib.Path("../../Vu2025").resolve()
profile_file = workdir / "9S9O-clean_complex_apo.cif"
ligand_file = workdir / "Vu2025_and_A1JMR.sdf"
network_file = workdir / "orion_edgemap_output.dat"

# protein

protein = openfe.ProteinComponent.from_pdbx_file(profile_file)

# ligands (Vu2025 + A1JMR)
ligands = [openfe.SmallMoleculeComponent.from_rdkit(m) for m in Chem.SDMolSupplier(ligand_file, removeHs=False)]

# Charging the ligands

# It is recommended to use a single set of charges for each ligand to ensure reproducibility between repeats 
# or consistent charges between different legs of a calculation involving the same ligand, 
# like a relative binding affinity calculation for example.
# Here we will use some utility functions from OpenFE which can assign partial charges to a series of molecules 
# with a variety of methods which can be configured via the OpenFFPartialChargeSettings class. 
# By default, ligands are charged using the am1bcc method from ambertools.

charged_ligands = bulk_assign_partial_charges(
    molecules=ligands,
    overwrite=False,
    method=charge_settings.partial_charge_method,
    toolkit_backend=charge_settings.off_toolkit_backend,
    generate_n_conformers=charge_settings.number_of_conformers,
    nagl_model=charge_settings.nagl_model,
    processors=1
)


# Creating the LigandNetwork

#mapper = openfe.LomapAtomMapper(max3d=1.0, element_change=False)
#scorer = openfe.lomap_scorers.default_lomap_score
#network_planner = openfe.ligand_network_planning.generate_minimal_spanning_network

#mapper = LomapAtomMapper(max3d=1.2, element_change=False)
mapper = KartografAtomMapper(
        atom_max_distance= 1.15, 
        atom_map_hydrogens= True,
        map_hydrogens_on_hydrogens_only = True,
        map_exact_ring_matches_only= True,
        allow_partial_fused_rings= True,
        allow_bond_breaks= False,
        )

print(f"creating ligand network using {network_file} ...")
ligand_network = load_custom_network_parallel(
        ligands=ligands, 
        mapper=mapper, 
        network_file=network_file,
        max_workers=20
        )

mapping = next(iter(ligand_network.edges))
#mapping.annotations # higher score is better

# Output setup for the network and transformations
network_setup_dir = pathlib.Path("network_setup")
network_setup_dir.mkdir(parents=True, exist_ok=True)
transformation_dir = network_setup_dir / "transformations"
transformation_dir.mkdir(parents=True, exist_ok=True)

with open(network_setup_dir / "ligand_network.graphml", mode='w') as f:
    f.write(ligand_network.to_graphml())


print("creating transformations ...")
transformations = []
for mapping in ligand_network.edges:
    for leg in ['solvent', 'complex']:
        # use the solvent and protein created above
        sysA_dict = {'ligand': mapping.componentA,
                     'solvent': solvent}
        sysB_dict = {'ligand': mapping.componentB,
                     'solvent': solvent}

        if leg == 'complex':
            # If this is a complex transformation we use the complex protocol
            # and add in the protein to the chemical states
            protocol = complex_protocol
            sysA_dict['protein'] = protein
            sysB_dict['protein'] = protein
        else:
            # If this is a solvent transformation we just use the solvent protocol
            protocol = solvent_protocol

        # we don't have to name objects, but it can make things (like filenames) more convenient
        sysA = openfe.ChemicalSystem(sysA_dict, name=f"{mapping.componentA.name}_{leg}")
        sysB = openfe.ChemicalSystem(sysB_dict, name=f"{mapping.componentB.name}_{leg}")

        prefix = "rbfe_"  # prefix is only to exactly reproduce CLI

        transformation = openfe.Transformation(
            stateA=sysA,
            stateB=sysB,
            mapping=mapping,
            protocol=protocol,  # use protocol created above
            name=f"{prefix}{sysA.name}_{sysB.name}"
        )
        transformations.append(transformation)
network = openfe.AlchemicalNetwork(transformations)


# then we write out each transformation
print(f"writing {len(transformations)} transformations ...")
for idx, transformation in enumerate(network.edges, start=1):
    filename = transformation_dir / f"{transformation.name}.json"
    print(f"  ({idx:2d}) {filename}")
    transformation.to_json(filename)
