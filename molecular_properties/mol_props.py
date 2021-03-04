# Import modules for our exercise
import numpy as np     # numerical package
import pandas as pd    # data organization package
import matplotlib.pyplot as plt # plotting package
import os              # operational system interface package
import sys

# Import modules for dealing with chemical information
from rdkit import Chem as Chem
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import AllChem as Chem2
from rdkit.Chem import Descriptors as Desc
from rdkit.Chem import Draw
from rdkit.Chem import rdmolfiles as RDFile

import pickle

import math
from collections import defaultdict

import os.path as op

input_filename=sys.argv[1]

# Function that reads multi-molecule MOL2 files. Adapted from:
# https://chem-workflows.com/articles/2019/07/18/building-a-multi-molecule-mol2-reader-for-rdkit/
# further adapted from function written by Guilherme Duarte, Rizzo Lab by John Bickel, Rizzo Lab
def mol2_mol_supplier_loop(file):
    ''' This function extracts all the molecules in the multi-molecule
        MOL2 file `file` and returns a list of rdkit.Chem.rdchem.mol 
        object.
        
        Variable         I/O          dtype           default value?
        ------------------------------------------------------------
        file              I           string                  None
        mols              O           list                    N/A
        mols[i]           O           rdkit.Chem.rdchem.mol   N/A
        
    '''
    mols=[]
    
    recording=False
    with open(file, 'r') as f:
        for line in f:
            
            # Determines if @<TRIPOS>MOLECULE is in line, which marks the start
            # of each molecule. Sets the recording variable to True, which is
            # the boolean to write each molecule.
            if ("@<TRIPOS>MOLECULE") in line:
                recording=True
                mol = []
            # Determines if "ROOT" is in line, which marks the end of each
            # molecule. Records the line and sets the recording variable
            # to false.
            elif ("ROOT") in line:
                mol.append(line)
                recording=False
                
                # Makes final adjustments to the data. It must look
                # like the MOL2 file of a single molecule.
                block = ",".join(mol).replace(',','')
                
                # Converts the data of a single molecule to a 
                # rdkit.Chem.rdchem.mol object.
                m=Chem.MolFromMol2Block(block,
                                        sanitize=False,
                                        cleanupSubstructures=False)
                mols.append(m)
                continue
                
            if recording==True:
                mol.append(line)
                
        return(mols)


def main()
	for mol in molecule_list:
	    mol.UpdatePropertyCache(strict=False)
	    Chem.SanitizeMol(mol,sanitizeOps=Chem.SanitizeFlags.SANITIZE_ALL^Chem.SanitizeFlags.SANITIZE_KEKULIZE^Chem.SanitizeFlags.SANITIZE_SETAROMATICITY)



main()