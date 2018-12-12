#CHOLVARS Merged Model
python ../dl_inputs_multitasked_negatives/generate_inputs.py --task_list /srv/scratch/annashch/cholvars/task_labels.unique.csv \
       --outf cholvars.chip.and.dnase.onevall.bed

#remove quotes (pandas is annoying and insists on placing quotes around the index labels)
sed -i 's/\"//g' cholvars.chip.and.dnase.onevall.bed

python /srv/scratch/annashch/deeplearning/form_inputs/code/bed_utils/get_train_valid_test_splits.py --source cholvars.chip.and.dnase.onevall.bed \
       --valid_chroms chr18 chr19 chr20 \
       --test_chroms chr17 chr21 chr22 \
       --out_prefix cholvars.chip.and.dnase.onevall
