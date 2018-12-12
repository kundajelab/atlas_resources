#Cholesterol model 
#python generate_inputs.py --task_list /srv/scratch/annashch/cholvars/task_labels.unique.csv \
#       --outf /srv/scratch/annashch/cholvars/cholvars.inputs.bed

#remove quotes (pandas is annoying and insists on placing quotes around the index labels)
#sed -i 's/\"//g' cholvars.inputs.bed

#python ../bed_utils/get_train_valid_test_splits.py --source /srv/scratch/annashch/cholvars/cholvars.inputs.bed \
#       --valid_chroms chr19 chr20 \
#       --test_chroms chr21 chr22 \
#       --out_prefix  /srv/scratch/annashch/cholvars/cholvars


#CHOLESTEROL DNASE
python generate_inputs.py --task_list /srv/scratch/annashch/cholvars/task_labels.unique.dnase.tsv \
       --outf /srv/scratch/annashch/cholvars/cholvars.dnase.inputs.bed

#remove quotes (pandas is annoying and insists on placing quotes around the index labels)
sed -i 's/\"//g' /srv/scratch/annashch/cholvars/cholvars.dnase.inputs.bed

python ../bed_utils/get_train_valid_test_splits.py --source /srv/scratch/annashch/cholvars/cholvars.dnase.inputs.bed \
       --valid_chroms chr19 chr20 \
       --test_chroms chr21 chr22 \
       --out_prefix  /srv/scratch/annashch/cholvars/cholvars.dnase
       



