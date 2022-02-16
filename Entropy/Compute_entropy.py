# -*- coding: utf-8 -*-

from Bio import AlignIO
from collections import Counter
import numpy as np


fastas = ["MLA.msa.relative_to_SR33.50.all.fas",
          "MLA.msa.relative_to_SR33.50.Sr50.fas",
          "MLA.msa.relative_to_SR33.50.Sr33.fas",
          "MLA.msa.relative_to_SR33.50.MLA.fas",
          "MLA.msa.relative_to_SR33.50.HcMLA.fas"]

output  = "test.out"

with open(output, "w") as o:
  o.write("Position\tEntropy\tType\n") # Header
  for item in fastas: #Iterate each group
    fasta_handle = AlignIO.read(item, "fasta") # read the MSA
    group = item.rsplit(".", 2)[1] # group name
    
    seqs = len(fasta_handle[:, 0]) # Number of  sequences
    cols = fasta_handle.get_alignment_length() # number of positions in MSA

    
    for i in range(cols): #Iterate all positions in the MSA
        gaps   = fasta_handle[:,i].count("-") # count number of gaps
        
        if gaps/float(seqs) >= 0.5:
            # gaps >= 0.5 -> skip entropy calculation. use 2.000 as a place holder
            o.write(f"{str(i + 1)}\t2.000\t{group}\n")
            
        else:
            # Adjust the number of sequences after removing the gaps
            num_seqs = len(fasta_handle[:, i].replace("-", ""))
            
            # Count amino acids 
            counts  =  Counter(fasta_handle[:, i].replace("-", ""))
            
            # Convert to the probabilities 
            Pi      = [ct/float(num_seqs) for ct in counts.values()]
            
            # Calculate normalized entropy 
            ent = sum([-1 * p * np.log2(p) / np.log2(20) for p in Pi])
            
            # Write the output
            o.write(f"{str(i + 1)}\t{str(ent)}\t{group}\n")

        