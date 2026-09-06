# Setup 

```sh
$ mamba activate openfe
(openfe) $
```

```sh
openfe plan-rbfe-network -M Vu2025_hybrid_docked.sdf -p 9S9P-clean_complex_relaxed_apo.cif -o network_setup --n-protocol-repeats 1 -s settings.yaml 
```

```sh
RBFE-NETWORK PLANNER
______________________

Parsing in Files: 
	Got input: 
		Small Molecules: SmallMoleculeComponent(name=Vu2025_13_1) SmallMoleculeComponent(name=Vu2025_12_1) SmallMoleculeComponent(name=Vu2025_11_1) SmallMoleculeComponent(name=Vu2025_10_1) SmallMoleculeComponent(name=Vu2025_22_1) SmallMoleculeComponent(name=Vu2025_14_1) SmallMoleculeComponent(name=Vu2025_02_1) SmallMoleculeComponent(name=Vu2025_21_1) SmallMoleculeComponent(name=Vu2025_08_1) SmallMoleculeComponent(name=Vu2025_03_1) SmallMoleculeComponent(name=Vu2025_04_1) SmallMoleculeComponent(name=Vu2025_01_1) SmallMoleculeComponent(name=Vu2025_05_1) SmallMoleculeComponent(name=Vu2025_06_1) SmallMoleculeComponent(name=Vu2025_07_1) SmallMoleculeComponent(name=Vu2025_09_1)
		ProteinComponent: ProteinComponent(name=)
		Cofactors: []
		Solvent: SolventComponent(name=O, Na+, Cl-)

Using Options:
	Mapper: <KartografAtomMapper-92be13375caab9a5f2ecbf75d925982f>
	Mapping Scorer: <function default_lomap_score at 0x7f3997dc4b80>
	Network Generation: functools.partial(<function generate_minimal_spanning_network at 0x7f3995669bc0>)
	Partial Charge Generation: nagl

	n_protocol_repeats=1 (1 simulation repeat(s) per transformation)

Planning RBFE-Campaign:
assigning ligand partial charges -- this may be slow
Generating charges: 100%|███████████████████████| 16/16 [00:16<00:00,  1.02s/it]
Mapping:  89%|██████████████████████████████████████████████████████████████████████████████████████▍          | 107/120 [00:01<00:00, 66.31it/s]Atom mapping for molA (name='Vu2025_01_1') to molB (name='Vu2025_09_1') failed after filters: 6 candidate atom pairs were found geometrically, but all were removed by configured filter rules. Returning an empty mapping. max_d=0.95, map_hydrogens=False
Mapping:  96%|████████████████████████████████████████████████████████████████████████████████████████████▉    | 115/120 [00:01<00:00, 66.66it/s]Atom mapping for molA (name='Vu2025_05_1') to molB (name='Vu2025_09_1') failed after filters: 4 candidate atom pairs were found geometrically, but all were removed by configured filter rules. Returning an empty mapping. max_d=0.95, map_hydrogens=False
Mapping: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 120/120 [00:01<00:00, 67.12it/s]
	Done

Output:
	Saving to: /home2/shbae/bit/openfe/nagl/network_setup
		- network_setup.json
		- ligand_network.graphml
				- rbfe_Vu2025_12_1_complex_Vu2025_11_1_complex.json
				- rbfe_Vu2025_13_1_complex_Vu2025_12_1_complex.json
				- rbfe_Vu2025_01_1_complex_Vu2025_05_1_complex.json
				- rbfe_Vu2025_11_1_complex_Vu2025_08_1_complex.json
				- rbfe_Vu2025_12_1_solvent_Vu2025_14_1_solvent.json
				- rbfe_Vu2025_12_1_solvent_Vu2025_22_1_solvent.json
				- rbfe_Vu2025_02_1_complex_Vu2025_03_1_complex.json
				- rbfe_Vu2025_11_1_complex_Vu2025_07_1_complex.json
				- rbfe_Vu2025_12_1_complex_Vu2025_22_1_complex.json
				- rbfe_Vu2025_11_1_solvent_Vu2025_08_1_solvent.json
				- rbfe_Vu2025_02_1_solvent_Vu2025_03_1_solvent.json
				- rbfe_Vu2025_12_1_complex_Vu2025_14_1_complex.json
				- rbfe_Vu2025_11_1_solvent_Vu2025_07_1_solvent.json
				- rbfe_Vu2025_07_1_solvent_Vu2025_09_1_solvent.json
				- rbfe_Vu2025_11_1_complex_Vu2025_01_1_complex.json
				- rbfe_Vu2025_12_1_complex_Vu2025_10_1_complex.json
				- rbfe_Vu2025_03_1_complex_Vu2025_04_1_complex.json
				- rbfe_Vu2025_21_1_solvent_Vu2025_06_1_solvent.json
				- rbfe_Vu2025_12_1_complex_Vu2025_02_1_complex.json
				- rbfe_Vu2025_12_1_solvent_Vu2025_11_1_solvent.json
				- rbfe_Vu2025_21_1_solvent_Vu2025_03_1_solvent.json
				- rbfe_Vu2025_13_1_solvent_Vu2025_12_1_solvent.json
				- rbfe_Vu2025_12_1_solvent_Vu2025_02_1_solvent.json
				- rbfe_Vu2025_11_1_solvent_Vu2025_01_1_solvent.json
				- rbfe_Vu2025_12_1_solvent_Vu2025_10_1_solvent.json
				- rbfe_Vu2025_03_1_solvent_Vu2025_04_1_solvent.json
				- rbfe_Vu2025_01_1_solvent_Vu2025_05_1_solvent.json
				- rbfe_Vu2025_21_1_complex_Vu2025_06_1_complex.json
				- rbfe_Vu2025_21_1_complex_Vu2025_03_1_complex.json
				- rbfe_Vu2025_07_1_complex_Vu2025_09_1_complex.json
	Duration: 0:00:25.341904
```

# Run

```sh
openfe quickrun network_setup/transformations/rbfe_Vu2025_01_1_solvent_Vu2025_05_1_solvent.json -o results/rbfe_Vu2025_01_1_solvent_Vu2025_05_1_solvent.json -d results/rbfe_Vu2025_01_1_solvent_Vu2025_05_1_solvent/
```

# Slurm Jobs

```
#!/usr/bin/bash

for file in network_setup/transformations/*.json; do
  name=${file:30}    # strip off parent path "network_setup/transformations/"
  prefix=${name%.*}  # strip off extension ".json"
  for r in {1..3}; do
      job="network_setup/transformations/${prefix}_${r}.job"
      cmd="openfe quickrun $file -o results/replicate_${r}/$name -d results/replicate_${r}/$prefix"
      echo -e "#!/usr/bin/env bash\n${cmd}" > $job
      #sbatch $job
  done
done
```
