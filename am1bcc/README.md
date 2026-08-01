```sh
$ openfe plan-rbfe-network -M ../Vu2025/Vu2025_9s9o_posit_docked.sdf -p ../Vu2025/9S9O-clean_complex_apo.cif --n-protocol-repeats 1 -o network_setup -s settings.yaml
RBFE-NETWORK PLANNER
______________________

Parsing in Files:
        Got input:
                Small Molecules: SmallMoleculeComponent(name=Vu2025_01_1) SmallMoleculeComponent(name=Vu2025_05_1) SmallMoleculeComponent(name=Vu2025_02_1) SmallMoleculeComponent(name=Vu2025_03_1) SmallMoleculeComponent(name=Vu2025_13_1) SmallMoleculeComponent(name=Vu2025_12_1) SmallMoleculeComponent(name=Vu2025_04_1) SmallMoleculeComponent(name=Vu2025_11_1) SmallMoleculeComponent(name=Vu2025_09_1) SmallMoleculeComponent(name=Vu2025_21_1) SmallMoleculeComponent(name=Vu2025_22_1) SmallMoleculeComponent(name=Vu2025_06_1) SmallMoleculeComponent(name=Vu2025_07_1) SmallMoleculeComponent(name=Vu2025_08_1) SmallMoleculeComponent(name=Vu2025_10_1) SmallMoleculeComponent(name=Vu2025_14_1)
                ProteinComponent: ProteinComponent(name=)
                Cofactors: []
                Solvent: SolventComponent(name=O, Na+, Cl-)

Using Options:
        Mapper: <KartografAtomMapper-b5e52cd8a03745cfcba064d52312ddea>
        Mapping Scorer: <function default_lomap_score at 0x7f1bbe95cae0>
        Network Generation: functools.partial(<function generate_minimal_spanning_network at 0x7f1bbc2a5b20>)
        Partial Charge Generation: am1bcc

        n_protocol_repeats=1 (1 simulation repeat(s) per transformation)

Planning RBFE-Campaign:
assigning ligand partial charges -- this may be slow
Generating charges: 100%|██████████████████████| 16/16 [30:44<00:00, 115.27s/it]
Mapping: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 120/120 [00:01<00:00, 62.64it/s]
        Done

Output:
        Saving to: /home2/shbae/bit/openferun/am1bcc/network_setup
                - network_setup.json
                - ligand_network.graphml
                                - rbfe_Vu2025_01_1_solvent_Vu2025_02_1_solvent.json
                                - rbfe_Vu2025_03_1_complex_Vu2025_06_1_complex.json
                                - rbfe_Vu2025_04_1_solvent_Vu2025_11_1_solvent.json
                                - rbfe_Vu2025_11_1_solvent_Vu2025_10_1_solvent.json
                                - rbfe_Vu2025_21_1_complex_Vu2025_22_1_complex.json
                                - rbfe_Vu2025_11_1_solvent_Vu2025_14_1_solvent.json
                                - rbfe_Vu2025_04_1_complex_Vu2025_11_1_complex.json
                                - rbfe_Vu2025_13_1_solvent_Vu2025_12_1_solvent.json
                                - rbfe_Vu2025_01_1_complex_Vu2025_03_1_complex.json
                                - rbfe_Vu2025_01_1_solvent_Vu2025_03_1_solvent.json
                                - rbfe_Vu2025_01_1_complex_Vu2025_02_1_complex.json
                                - rbfe_Vu2025_13_1_complex_Vu2025_08_1_complex.json
                                - rbfe_Vu2025_01_1_complex_Vu2025_05_1_complex.json
                                - rbfe_Vu2025_11_1_complex_Vu2025_10_1_complex.json
                                - rbfe_Vu2025_13_1_complex_Vu2025_22_1_complex.json
                                - rbfe_Vu2025_03_1_solvent_Vu2025_06_1_solvent.json
                                - rbfe_Vu2025_21_1_solvent_Vu2025_22_1_solvent.json
                                - rbfe_Vu2025_09_1_complex_Vu2025_07_1_complex.json
                                - rbfe_Vu2025_09_1_solvent_Vu2025_07_1_solvent.json
                                - rbfe_Vu2025_03_1_complex_Vu2025_07_1_complex.json
                                - rbfe_Vu2025_11_1_solvent_Vu2025_22_1_solvent.json
                                - rbfe_Vu2025_11_1_complex_Vu2025_22_1_complex.json
                                - rbfe_Vu2025_13_1_solvent_Vu2025_08_1_solvent.json
                                - rbfe_Vu2025_03_1_solvent_Vu2025_07_1_solvent.json
                                - rbfe_Vu2025_02_1_solvent_Vu2025_11_1_solvent.json
                                - rbfe_Vu2025_13_1_complex_Vu2025_12_1_complex.json
                                - rbfe_Vu2025_01_1_solvent_Vu2025_05_1_solvent.json
                                - rbfe_Vu2025_02_1_complex_Vu2025_11_1_complex.json
                                - rbfe_Vu2025_11_1_complex_Vu2025_14_1_complex.json
                                - rbfe_Vu2025_13_1_solvent_Vu2025_22_1_solvent.json
        Duration: 0:30:53.344871
```
