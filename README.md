# Open-Source Binding Free Energy

Considered Open-Source Frameworks

| Framework | MD Engine | Remarks | License |
| --------- | --------- | ------- | ------- |
| [OpenFE](https://github.com/OpenFreeEnergy/openfe) | OpenMM | Equilibrium method | MIT license |
| [PMX](https://github.com/degrootlab/pmx) | Gromacs | Non-Equilibrium method | LGPL-3.0 |
| [Timemachine](https://github.com/proteneer/timemachine) | OpenMM | | Apache License, Version 2.0 |


# Test Dataset


## Reference protein-ligand complex, Vu2025

Crystal structure of p53 Y220C mutant in complex with Rezatapopt (PDB id: 9S9O, ligand residue name: A1JMR)

Vu BT, Dominique R, Fahr BJ, Li HH, Fry DC, Xu L, Yang H, Puzio-Kuter A, Good A, Liu B, Huang KS, Tanaka N, Davis TW, Dumble ML. Discovery of Rezatapopt (PC14586), a First-in-Class, Small-Molecule Reactivator of p53 Y220C Mutant in Development. ACS Med Chem Lett. 2024 Nov 4;16(1):34-39. doi: 10.1021/acsmedchemlett.4c00379. PMID: 39811143; PMCID: PMC11726359.


## Receptor

The protein-ligand complex structures were processed by [mdworks](https://github.com/sunghunbae/mdworks) (see below). Use `9S9O-clean_complex_relaxed_apo.pdb` or `9S9O-clean_complex_relaxed_apo.cif` for ligand-removed or apo protein structure.

```sh
# 9S9O
$ pip install mdworks
$ cd Vu2025/
$ mdworks ready 9S9O-clean.cif --ligand A1JMR
$ mdworks relax 9S9O-clean_complex.cif --ligand A1JMR
# output files:
#    9S9O-clean_complex_relaxed.cif.gz 
#    9S9O-clean_complex_relaxed.pdb.gz 
$ mdworks delete 9S9O-clean_complex_relaxed.cif.gz A1JMR --tag apo
2026-07-28 11:17:INFO:mdworks.editor:select residues: {'C': 1} (70 atoms)
2026-07-28 11:17:INFO:mdworks.editor:remove selected
2026-07-28 11:17:INFO:mdworks.editor:write to 9S9O-clean_complex_relaxed_apo.cif
```

## Ligands

Rezatapopt hit-to-lead series were extracted from Vu2025 (see `Vu2025.smi`). Use `Vu20205_and_A1JMR.sdf` for ligands input which contains both the reference (Rezatapopt) and compounds series.

| Ligands | Note |
| ------- | ---- |
| Vu20205_and_A1JMR.sdf | Included both the reference and subject compounds. Use this file as ligands input |
| Vu2025_posit_docked.sdf | OE POSIT with 9S9O as receptor; no relax;`-outputall`|
