# Install OpenFE

```sh
$ mamba create -n openfe cuda-version=13.1 openfe
$ mamba activate openfe
$ pip install mdworks
```

# Vu2025/

## Reference Protein-ligand Complex 

| PDB id | Description |
| ------ | ----------- |
| 9S9P   | crystal structure of p53 Y220S mutant in complex with Rezatapopt |
| 9S9O   | crystal structure of p53 Y220C mutant in complex with Rezatapopt |

Vu BT, Dominique R, Fahr BJ, Li HH, Fry DC, Xu L, Yang H, Puzio-Kuter A, Good A, Liu B, Huang KS, Tanaka N, Davis TW, Dumble ML. Discovery of Rezatapopt (PC14586), a First-in-Class, Small-Molecule Reactivator of p53 Y220C Mutant in Development. ACS Med Chem Lett. 2024 Nov 4;16(1):34-39. doi: 10.1021/acsmedchemlett.4c00379. PMID: 39811143; PMCID: PMC11726359.


## Receptor Structure Preparation

The protein-ligand complex structures were processed by [mdworks](https://github.com/sunghunbae/mdworks). Remove the rezataopopt from `9S9O-clean_complex_relaxed.cif.gz` or `9S9O-clean_complex_relaxed.pdb.gz` and use as receptor for OpenFE.

```sh
$ pip install mdworks
```

```sh
# 9S9P
$ mdworks ready 9S9P-clean.cif --ligand A1JMR

$ mdworks relax 9S9P-clean_complex.cif --ligand A1JMR
# target output files:
#    9S9P-clean_complex_relaxed.cif.gz 
#    9S9P-clean_complex_relaxed.pdb.gz 

$ mdworks delete 9S9P-clean_complex_relaxed.cif.gz A1JMR --tag apo
2026-07-28 11:17:INFO:mdworks.editor:select residues: {'C': 1} (70 atoms)
2026-07-28 11:17:INFO:mdworks.editor:remove selected
2026-07-28 11:17:INFO:mdworks.editor:write to 9S9P-clean_complex_relaxed_apo.cif

# target output file:
#    9S9P-clean_complex_relaxed_apo.cif

# 9S9O
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

## Ligands Preparation

Rezatapopt series were extracted from Vu2025 (see `Vu2025.smi`)
Ligands were docked to 9S9P using OE HYBRID. 
Use `hybrid_docked.sdf.gz` for OpenFE.
