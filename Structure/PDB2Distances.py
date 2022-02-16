# -*- coding: utf-8 -*-

from Bio.PDB import PDBParser

# read the coordinates from the file
parser    = PDBParser()
structure = parser.get_structure('Sr50', 'Sr50.Alphafold.pdb')
output    = "Sr50.pairwise_distances.min8.list"

model = structure[0]
chain = model['A']

with open(output, "w") as o:
  o.write("Residue1\tResidue2\tDistance\n") # header
  for res1 in chain:
      for res2 in chain:
         if res1 != res2: # Ignore dianonal
           try:
             distance = res1['CA'] - res2['CA']
             if distance <= 8: #Ignore long distances
                o.write(f"{res1.id[1]}\t{res2.id[1]}\t{distance}\n")
           except KeyError: # In cases there are no 'CA'
              continue
            
