#CHOLVARS Merged Model
python /srv/scratch/annashch/deeplearning/form_inputs/code/dl_inputs_whole_genome_tiled/generate_inputs_tiled_whole_genome_fast.py --task_list /srv/scratch/annashch/cholvars/task_labels.unique.csv \
       --outf cholvars.chip.and.dnase.tiled.wholegenome.bed --bins /srv/scratch/annashch/deeplearning/form_inputs/code/dl_inputs_whole_genome_tiled/hg19.bins.bed.gz --training_bin_size=1000 --threads 40

#remove quotes (pandas is annoying and insists on placing quotes around the index labels)
sed -i 's/\"//g' cholvars.chip.and.dnase.tiled.wholegenome.bed

python /srv/scratch/annashch/deeplearning/form_inputs/code/bed_utils/get_train_valid_test_splits.py --source cholvars.chip.and.dnase.tiled.wholegenome.bed \
       --valid_chroms chr18 chr19 chr20 \
       --test_chroms chr17 chr21 chr22 \
       --out_prefix cholvars.chip.and.dnase.tiled.wholegenome
