# Building GROMACS

```bash
$ tar xfz gromacs-2026.3.tar.gz

$ cd gromacs-2026.3

$ mkdir build

$ cd build

$ cmake .. \
	-DGMX_BUILD_OWN_FFTW=ON \
	-DGMX_FFT_LIBRARY=fftw3 \
	-DREGRESSIONTEST_DOWNLOAD=ON \
	-DGMX_GPU=CUDA \
	-DBUILD_SHARED_LIBS=off \
	-DCMAKE_INSTALL_PREFIX=/home2/shbae/local/gromacs

$ make -j

# test built gromacs
$ make check

$ make install

$ source /home2/shbae/ocal/gromacs/bin/GMXRC
```


# Installing PMX

```bash
$ mamba create -n pmx python=3.12 -y
$ mamba activate pmx
(pmx) $ mamba install numpy scipy matplotlib rdkit
(pmx) $ git clone https://github.com/deGrootLab/pmx pmx
(pmx) $ cd pmx

# The 'master' branch is written in Python 2. 
# For Python 3 version and Icolos support use 'develop' branch; 
# to switch to 'develop' branch type:

(pmx) $ git checkout develop
(pmx) $ python setup.py install
```

# Non-Equilibrium Switching Framwork

- Two 6 ns long equilibrium simulations will be performed in the physical states A and B. This will be done for the ligand solvated in water and protein-ligand complex.
- We will extract snapshots from the equilibrium simulations and run 80 rapid (50 ps each) transitions in the directions A->B and A<-B.
- During the transitions, we will record the work required for the ligand morphing. 
- The work will be related to ΔG by applying Crooks fluctuation theorem.

[2024 Tutorial](http://pmx.mpibpc.mpg.de/Tutorial2024/Baltic_HPC2024/ligand_tutorial.html)


# TODO

It seems feasible to build openfe-like workflow based on gromacs and pmx

- automated parametrization (mdworks)
- fast transition


## Workflow to Transition from OpenFE to PMX

1. Extract edges from OpenFE

	Iterate through the edges of your LigandNetwork to identify each pairwise transformation (Ligand A \(\rightarrow \) Ligand B).
	[1] (https://github.com/OpenFreeEnergy/openfe/discussions/1180)

2. Export ligand coordinates and structures

	Save the individual ligand molecules (SmallMoleculeComponent) from your OpenFE nodes into standard coordinate formats (such as PDB or SDF/mol2).
	[1] (https://docs.openfree.energy/en/v1.0.0/guide/setup/creating_ligand_networks.html)
	[2] (https://github.com/OpenFreeEnergy/openfe/discussions/1180)

3. Assign GROMACS-compatible parameters

	Parameterize the individual ligands for GROMACS using tools compatible with PMX (e.g., Antechamber/ACPYPE for GAFF/GAFF2 or CGenFF).
	[1] (https://bioexcel.eu/pmx-new/)
	[2] (https://www.nature.com/articles/s42004-023-00859-9)
	[3] (https://deepforestsci.com/blog/7)

4. Perform atom mapping with PMX

	Run PMX's atom mapper (pmx atomMapper or equivalent ligand-to-ligand alignment scripts) on each extracted pair, or export OpenFE's mapping if format converters are written. PMX requires its own atom correspondence mapping to create hybrid topologies.
	[1] (https://pmc.ncbi.nlm.nih.gov/articles/PMC8145179/)
	[2] (https://www.nature.com/articles/s42004-023-00859-9)

5. Generate hybrid topologies

	Use PMX's ligand hybrid generation utility (pmx ligandHybrid) to build the dual-topology/hybrid files (topol.top, coordinate files) for GROMACS.
	[1] (https://bioexcel.eu/pmx-new/)
	[2] (https://www.nature.com/articles/s42004-023-00859-9)

6. Run GROMACS simulations

	Execute equilibrium or non-equilibrium (fast-growth) alchemical staging using GROMACS and extract \(\Delta G\) values for each edge. 
	[1] (https://yorkgrouptutorials-db4433.gitlab.io/WorkshopTutorials/2026_Amber_Workshop_SSB/Day4/HandsOn9-RBFE.html)
	[2] (https://bioexcel.eu/pmx-new/)

6. Analyze the network
	Combine the resulting edge \(\Delta G\) values using network analysis tools like Cinnabar to compute the overall maximum-likelihood binding affinities.
	[1] (https://yorkgrouptutorials-db4433.gitlab.io/WorkshopTutorials/2026_Amber_Workshop_SSB/Day4/HandsOn9-RBFE.html)
