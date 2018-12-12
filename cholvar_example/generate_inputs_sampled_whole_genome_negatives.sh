#!/bin/bash
#generate 1 million 1kb regions from hg19
python /users/annashch/anna_utils/seq_utils/sample_genome_randomly.py --outf wholegenome.hg19.1M.1kb.bed

#filter genome regions to just 600000 negatives
bedtools intersect -v -a wholegenome.hg19.1M.1kb.bed -b cholvars.chip.and.dnase.onevall.universalneg.bed | head -n 600000 > wholegenome.hg19.600k.negatives.bed

#add 0 labels 
python /users/annashch/anna_utils/seq_utils/add_fixed_labels_to_bed.py --bed wholegenome.hg19.600k.negatives.bed  --labels 0 --ntasks 298 --outf tmp 
mv tmp wholegenome.hg19.600k.negatives.bed

#add the whole genome negatives to the onevall/univeral negative matrix
cat cholvars.chip.and.dnase.onevall.universalneg.bed wholegenome.hg19.600k.negatives.bed  > cholvars.chip.and.dnase.onevall.universalneg.wholegenomeneg.bed

#shuffle!
python /users/annashch/anna_utils/seq_utils/sample_bed_file_randomly.py --bed cholvars.chip.and.dnase.onevall.universalneg.wholegenomeneg.bed --outf tmp --header
mv tmp cholvars.chip.and.dnase.onevall.universalneg.wholegenomeneg.bed

#generate a train/test/validation split
python /srv/scratch/annashch/deeplearning/form_inputs/code/bed_utils/get_train_valid_test_splits.py --source cholvars.chip.and.dnase.onevall.universalneg.wholegenomeneg.bed \
       --valid_chroms chr18 chr19 chr20 \
       --test_chroms chr17 chr21 chr22 \
       --out_prefix cholvars.chip.and.dnase.onevall.universalneg.wholegenomeneg


