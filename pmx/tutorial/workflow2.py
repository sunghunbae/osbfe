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


fe = AZtutorial()

# set the workpath
fe.workPath = 'workpath'
# set the path to the molecular dynamics parameter files
fe.mdpPath = 'input/mdppath'
# set the number of replicas (several repetitions of calculation are useful to obtain reliable statistics)
fe.replicas = 1
# provide the path to the protein structure and topology
fe.proteinPath = 'input/protein_amber'
# provide the path to the folder with ligand structures and topologies
fe.ligandPath = 'input/ligands'
# provide edges
fe.edges = [ ['18625-1','18626-1'] ]

# fe.replicas = 1
# fe.workPath = 'workpath_precalculated'

fe.prepare_transitions( bGenTpr=True, bProt=False )
fe.run_simulation_locally(simType='transitions', bVerbose=True)

# fe.JOBsimcpu = 2
# fe.JOBqueue = 'SGE'
# fe.JOBsource = ['/etc/profile.d/modules.sh','/usr/local/gromacs/GMXRC2018']
# fe.JOBmodules = ['shared','owl/intel-mpi-default','cuda91']
# fe.JOBgpu = True
# fe.JOBgmx = 'mdrun_threads'
# fe.prepare_jobscripts(simType='transitions', bProt=False)

fe.run_analysis( bVerbose=True)