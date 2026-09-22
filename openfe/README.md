# Install OpenFE

```sh
$ mamba create -n openfe cuda-version=13.1 openfe
$ mamba activate openfe
$ pip install mdworks
```

# Prepared Dataset Ready to Run

| Folder | Network Setup | Atomic Charge | Note |
| ------ | ------------- | ------------- | ---- |
| `am1bcc` | OpenFE default | AM1BCC | OpenFE default setting |
| `nagl` | OpenFE default | NAGL | |
| `orion_am1bcc` | OpenEye Orion OE-LOMAP | AM1BCC | Use this dataset for OE comparison |
| `orion_nagl` | OpenEye Orion OE-LOMAP | NAGL | |


## Run the simulations

Below is an example of individual run using `openfe quickrun` command:

```sh
$ cd orion_am1bcc/
$ openfe quickrun \
       network_setup/transformations/rbfe_Vu2025_01_1_complex_Vu2025_05_1_complex.json \
       -o one/one_results.json \
       -d one
```

Below is an example of simple SLURM job script:

```sh
for file in network_setup/transformations/*.json; do
  relpath=${file:30}  # strip off "network_setup/transformations/"
  dirpath=${relpath%.*}  # strip off final ".json"
  for repeat in {1..3}; do
      jobpath="network_setup/transformations/${dirpath}_${repeat}.job"
      cmd="openfe quickrun $file -o results/repeat${repeat}/$relpath -d results/repeat${repeat}/$dirpath"
      echo -e "#!/usr/bin/env bash\n${cmd}" > $jobpath
      sbatch $jobpath
  done
done
```

## Gather the results

To gather all the $\Delta G$ estimates into a single file, use `openfe gather` command from within the
working directory:

```sh
openfe gather results/ --report dg -o final_results.tsv
```


# Network Setup

1. Use apo receptor structure
1. Ligands should include reference molecule in RBFE
1. Use `--n-protocol-repeats 1`

## Using NAGL charge (est. <3 min)

```sh
$ cd openfe/nagl
$ openfe plan-rbfe-network \
	-M ../../Vu2025/Vu2025_and_A1JMR.sdf \
	-p ../../Vu2025/9S9O-clean_complex_apo.cif \
	-o network_setup \
	--n-protocol-repeats 1 \
	-s settings.yaml

#<setttings.yaml>

mapper:
    method: kartograf
    settings:
        #atom_max_distance: 0.95
        atom_max_distance: 1.15
        atom_map_hydrogens: true
        map_hydrogens_on_hydrogens_only: true
        map_exact_ring_matches_only: true
        allow_partial_fused_rings: true
        allow_bond_breaks: false

network:
    method: generate_minimal_spanning_network

partial_charge:
    # method: am1bcc
    # method: am1bccelf10
    # method: espaloma
    method: nagl
    settings:
        # off_toolkit_backend: ambertools
        # off_toolkit_backend: openeye  # required for the am1bccelf10 method
        number_of_conformers: null  # null specifies the use of the input conformer, a value requests that a new conformer be generated
        nagl_model: null  # null specifies the use of the latest nagl model
```

## Using AM1BCC charge (est. 20-40 min)

```sh
$ nohup openfe plan-rbfe-network \
	-M ../../Vu2025/Vu2025_and_A1JMR.sdf \
	-p ../../Vu2025/9S9O-clean_complex_apo.cif \
	--n-protocol-repeats 1 \
	-o network_setup \
	-s settings.yaml &


#<settings.yaml>

mapper:
    method: kartograf
    settings:
        #atom_max_distance: 0.95
        atom_max_distance: 1.15
        atom_map_hydrogens: true
        map_hydrogens_on_hydrogens_only: true
        map_exact_ring_matches_only: true
        allow_partial_fused_rings: true
        allow_bond_breaks: false

network:
    method: generate_minimal_spanning_network

partial_charge:
    method: am1bcc
    # method: am1bccelf10
    # method: espaloma
    #method: nagl
    settings:
        # off_toolkit_backend: ambertools
        # off_toolkit_backend: openeye  # required for the am1bccelf10 method
        number_of_conformers: null  # null specifies the use of the input conformer, a value requests that a new conformer be generated
        nagl_model: null  # null specifies the use of the latest nagl model
```

## Using Orion edgemapper output with NAGL charges

```sh
$ cd  orion_nagl/
$ python plan_oe_network.py
```

## Using Orin edgemapper outout with AM1BCC charges

```sh
$ cd origon_am1bcc/
$ nohup python plan_oe_network.py &
```


## About `--n-protocol-repeats 1`

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
