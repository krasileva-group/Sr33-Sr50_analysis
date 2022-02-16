#Reformat and filter the MSA from alphafold
#Change sto to a3m
reformat.pl uniref90_hits.sto uniref90_hits.a3m

#Reduce redundancy with hhfilter
hhfilter -id 95 -cov 75 -i uniref90_hits.a3m -o uniref90_hits.filtered.a3m

#Change to fasta. The output in this step is attatched
reformat.pl -i uniref90_hits.filtered.a3m -o uniref90_hits.filtered.fasta

# Run pydca
pydca trim_by_refseq protein uniref90_hits.filtered.fasta SR50.fasta --remove_all --verbose
cd Trimmed_uniref90_hits.filtered
plmdca compute_fn protein Trimmed_uniref90_hits.filtered.fa --max_iterations 1000 --num_threads 28 --apc --verbose