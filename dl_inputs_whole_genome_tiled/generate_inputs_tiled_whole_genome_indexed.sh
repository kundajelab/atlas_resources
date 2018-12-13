python generate_inputs_tiled_whole_genome_indexed.py --task_list tasks.tsv \
       --out_bed labels.tsv \
       --chrom_sizes hg38.chrom.sizes \
       --stride 50 \
       --bin_size 1000 \
       --bin_center_size 200 \
       --threads 1 \
       --allow_ambiguous \
       --labeling_approach peak_summit_near_bin_center

