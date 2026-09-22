import pmx
from pmx.utils import create_folder
from pmx import gmx, ligand_alchemy, jobscript
import sys
import matplotlib.pyplot as plt
import numpy as np
import os,shutil
import re
import subprocess
import glob
import random
import pandas as pd
from AZtutorial import *

# step 0

# initialize the free energy environment object: it will store the main parameters for the calculations
fe = AZtutorial()

# set the workpath
fe.workPath = 'workpath'
# set the path to the molecular dynamics parameter files
fe.mdpPath = 'input/mdppath'
# set the number of replicas (several repetitions of calculation are useful to obtain reliable statistics)
fe.replicas = 3
# provide the path to the protein structure and topology
fe.proteinPath = 'input/protein_amber'
# provide the path to the folder with ligand structures and topologies
fe.ligandPath = 'input/ligands'
# provide edges
fe.edges = [ ['18625-1','18626-1'] ]

# finally, let's prepare the overall free energy calculation directory structure
fe.prepareFreeEnergyDir()

# 1a. Firstly, let's create a hybrid structure/topology for the two ligands forming an edge. 
fe.atom_mapping(bVerbose=False)

# 1b. Secondly, we will construct a hybrid structure and topology based on the established mapping
fe.hybrid_structure_topology(bVerbose=False)

# 1c. Finally, we assemble the ligand and ligand+protein systems, 
# i.e. create structures and topologies that will be used further in the step 2.
fe.assemble_systems()

# Step 2. Prepare equilibrium simulations.
fe.boxWaterIons()

fe.prepare_simulation( simType='em' )
fe.run_simulation_locally( simType='em', bProt=False, bVerbose=True )

fe.prepare_simulation( simType='eq_nvt', bProt=False)
fe.run_simulation_locally( simType='eq_nvt', bProt=False, bVerbose=True )

fe.prepare_simulation( simType='eq', bProt=False)
fe.prepare_jobscripts(simType='eq')