# Vu2025/

## Reference protein-ligand complex 

| PDB id | Description |
| ------ | ----------- |
| 9S9P   | crystal structure of p53 Y220S mutant in complex with Rezatapopt |
| 9S9O   | crystal structure of p53 Y220C mutant in complex with Rezatapopt |

Vu BT, Dominique R, Fahr BJ, Li HH, Fry DC, Xu L, Yang H, Puzio-Kuter A, Good A, Liu B, Huang KS, Tanaka N, Davis TW, Dumble ML. Discovery of Rezatapopt (PC14586), a First-in-Class, Small-Molecule Reactivator of p53 Y220C Mutant in Development. ACS Med Chem Lett. 2024 Nov 4;16(1):34-39. doi: 10.1021/acsmedchemlett.4c00379. PMID: 39811143; PMCID: PMC11726359.


## Receptor

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

## Ligands

Rezatapopt series were extracted from Vu2025 (see `Vu2025.smi`)

| Ligands | Method | Receptor |
| ------- | ------ | -------- |
| Vu2025_hybrid_docked.sdf | OE HYBRID | 9S9P |
| Vu2025_posit_docked.sdf  | OE POSIT  | 9S9O; no relax;`-outputall`; FE-NES floe |


# Install OpenFE

```sh
$ mamba create -n openfe cuda-version=13.1 openfe
$ mamba activate openfe
$ pip install mdworks
```


## Console Output (without `--n-protocol-repeats 1`)

If we set up the network by `openfe plan-rbfe-network -M <ligands.sdf> -p <protein.pdb> -o network_setup/` 
without `--n-protocol-repeats 1` option, default behavior is to run 3 replicate simulations in a set and report dG.
Because each MD is independent, using `--n-protocol-repeats 1` is more compute-efficient.

Note: openfe’s default behaviour is to use three repeats to calculate the uncertainty (i.e. standard deviation) in an estimate. When setting `--n-protocol-repeats 1`, you must execute the transformation multiple times - at minimum 2, but best practice is 3 independent repeats.


```bash
openfe quickrun \
       network_setup/transformations/rbfe_Vu2025_01_1_complex_Vu2025_05_1_complex.json \
       -o one/one_results.json \
       -d one

Current directory: /home2/shbae/bit/openfe.1/test/
Using existing working directory: one/
Loading transformation from: network_setup/transformations/rbfe_Vu2025_01_1_complex_Vu2025_05_1_complex.json
When simulation is complete, results will be written to: one/one_results.json

If this simulation is interrupted or fails, you may attempt to resume execution using:
openfe quickrun network_setup/transformations/rbfe_Vu2025_01_1_complex_Vu2025_05_1_complex.json -o one/one_results.json -d one --resume

Planning simulations for this edge...

Starting the simulations for this edge...

An online_analysis_interval that is not a multiple of the checkpoint_interval can lead to redundant information in the real time yaml file after recovering from checkpoints.
Please cite the following:

        Friedrichs MS, Eastman P, Vaidyanathan V, Houston M, LeGrand S, Beberg AL, Ensign DL, Bruns CM, and Pande VS. Accelerating molecular dynamic simulations on graphics processing unit. J. Comput. Chem. 30:864, 2009. DOI: 10.1002/jcc.21209
        Eastman P and Pande VS. OpenMM: A hardware-independent framework for molecular simulations. Comput. Sci. Eng. 12:34, 2010. DOI: 10.1109/MCSE.2010.27
        Eastman P and Pande VS. Efficient nonbonded interactions for molecular dynamics on a graphics processing unit. J. Comput. Chem. 31:1268, 2010. DOI: 10.1002/jcc.21413
        Eastman P and Pande VS. Constant constraint matrix approximation: A robust, parallelizable constraint method for molecular simulations. J. Chem. Theor. Comput. 6:434, 2010. DOI: 10.1021/ct900463w
        Chodera JD and Shirts MR. Replica exchange and expanded ensemble simulations as Gibbs multistate: Simple improvements for enhanced mixing. J. Chem. Phys., 135:194110, 2011. DOI:10.1063/1.3660669
        
An online_analysis_interval that is not a multiple of the checkpoint_interval can lead to redundant information in the real time yaml file after recovering from checkpoints.
Please cite the following:

        Friedrichs MS, Eastman P, Vaidyanathan V, Houston M, LeGrand S, Beberg AL, Ensign DL, Bruns CM, and Pande VS. Accelerating molecular dynamic simulations on graphics processing unit. J. Comput. Chem. 30:864, 2009. DOI: 10.1002/jcc.21209
        Eastman P and Pande VS. OpenMM: A hardware-independent framework for molecular simulations. Comput. Sci. Eng. 12:34, 2010. DOI: 10.1109/MCSE.2010.27
        Eastman P and Pande VS. Efficient nonbonded interactions for molecular dynamics on a graphics processing unit. J. Comput. Chem. 31:1268, 2010. DOI: 10.1002/jcc.21413
        Eastman P and Pande VS. Constant constraint matrix approximation: A robust, parallelizable constraint method for molecular simulations. J. Chem. Theor. Comput. 6:434, 2010. DOI: 10.1021/ct900463w
        Chodera JD and Shirts MR. Replica exchange and expanded ensemble simulations as Gibbs multistate: Simple improvements for enhanced mixing. J. Chem. Phys., 135:194110, 2011. DOI:10.1063/1.3660669
        
An online_analysis_interval that is not a multiple of the checkpoint_interval can lead to redundant information in the real time yaml file after recovering from checkpoints.
Please cite the following:

        Friedrichs MS, Eastman P, Vaidyanathan V, Houston M, LeGrand S, Beberg AL, Ensign DL, Bruns CM, and Pande VS. Accelerating molecular dynamic simulations on graphics processing unit. J. Comput. Chem. 30:864, 2009. DOI: 10.1002/jcc.21209
        Eastman P and Pande VS. OpenMM: A hardware-independent framework for molecular simulations. Comput. Sci. Eng. 12:34, 2010. DOI: 10.1109/MCSE.2010.27
        Eastman P and Pande VS. Efficient nonbonded interactions for molecular dynamics on a graphics processing unit. J. Comput. Chem. 31:1268, 2010. DOI: 10.1002/jcc.21413
        Eastman P and Pande VS. Constant constraint matrix approximation: A robust, parallelizable constraint method for molecular simulations. J. Chem. Theor. Comput. 6:434, 2010. DOI: 10.1021/ct900463w
        Chodera JD and Shirts MR. Replica exchange and expanded ensemble simulations as Gibbs multistate: Simple improvements for enhanced mixing. J. Chem. Phys., 135:194110, 2011. DOI:10.1063/1.3660669
        
Done with all simulations! Analyzing the results....
Here is the result:
	dG = 39.53214427813803 kilocalorie_per_mole ± 0.38406561279511076 kilocalorie_per_mole


	Duration: 9:27:16.584682
```
