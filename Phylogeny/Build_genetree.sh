#Infer the MLA family tree
mafft --maxiterate 1000 --globalpair --thread 20 MLA_family.fasta > MLA_family.msa.fasta
trimal -gt 0.3 -in MLA_family.msa.fasta -out MLA_family.msa.filtered.fasta
fasttree -slow < MLA_family.msa.filtered.fasta > MLA_family_phylogeny.nwk