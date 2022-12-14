# -*- coding: utf-8 -*-

import numpy
from Bio.PDB import PDBParser

# create parser
parser = PDBParser()

# read structure from file
structure = parser.get_structure('Sr50', 'ranked_0.pdb')

model = structure[0]
chain = model['A']

o = open("Sr50.pairwise_distances.min8.list", "w")
o.write("Residue1\tResidue2\tDistance\n")

for residue1 in chain:
    for residue2 in chain:
            # compute distance between CA atoms
                
            if residue1.id[1] < residue2.id[1]:
                #Long range contact or inter-domain contact
                if (residue2.id[1] - residue1.id[1]) > 24 \
                    or (residue1.id[1] <= 176 & residue2.id[1] > 176) \
                    or (176 < residue1.id[1] <= 521 & residue2.id[1] > 521):
                        
                    try:
                        if residue1.resname == 'GLY':
                            res1_pos = residue1['CA'].get_coord()
                        else:
                            res1_pos = residue1['CB'].get_coord()
                            
                        if residue1.resname == 'GLY':
                            res2_pos = residue2['CA'].get_coord()
                        else:
                            res2_pos = residue2['CB'].get_coord()
                            
                        distance = numpy.linalg.norm(res2_pos - res1_pos)
                        
                        if distance <= 8:
                            o.write(f"{residue1.id[1]}\t{residue2.id[1]}\t{distance}\n")
                    except KeyError:
                        ## no CA atom, e.g. for H_NAG
                        continue
                    
o.close()

