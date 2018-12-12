#!/bin/bash
bedtools intersect -v -a ../encode-roadmap.dnase.master.bed -b cholvars.chip.and.dnase.onevall.bed > universal_negatives_minus_cholvars.bed

#randomly sample 200k universal negatives
python /users/annashch/anna_utils/seq_utils/sample_bed_file_randomly.py --n 200000 --bed universal_negatives_minus_cholvars.bed --outf universal_negatives_minus_cholvars.200k.bed

#pad the universal negatives out to 1kb
python /users/annashch/anna_utils/seq_utils/pad.py --input_bed universal_negatives_minus_cholvars.200k.bed --desired_length 1000 --output_bed universal_negatives_minus_cholvars.200k.1kb.bed --chromsizes /mnt/data/annotations/by_release/hg19.GRCh37/hg19.chrom.sizes 


#add 0 labels 
python /users/annashch/anna_utils/seq_utils/add_fixed_labels_to_bed.py --bed universal_negatives_minus_cholvars.200k.bed --labels 0 --ntasks 298 --outf tmp 
mv tmp universal_negatives_minus_cholvars.200k.bed

#add the universal negatives to the onevall matrix
cat cholvars.chip.and.dnase.onevall.bed universal_negatives_minus_cholvars.200k.bed > cholvars.chip.and.dnase.onevall.universalneg.bed

#shuffle!
python /users/annashch/anna_utils/seq_utils/sample_bed_file_randomly.py --bed cholvars.chip.and.dnase.onevall.universalneg.bed --outf tmp --header
mv tmp cholvars.chip.and.dnase.onevall.universalneg.bed

#generate a train/test/validation split
python /srv/scratch/annashch/deeplearning/form_inputs/code/bed_utils/get_train_valid_test_splits.py --source cholvars.chip.and.dnase.onevall.universalneg.bed \
       --valid_chroms chr18 chr19 chr20 \
       --test_chroms chr17 chr21 chr22 \
       --out_prefix cholvars.chip.and.dnase.onevall.universalneg
