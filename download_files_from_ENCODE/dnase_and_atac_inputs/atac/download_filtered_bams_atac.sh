python download_filtered_bams_atac.py
split -d -a3 -l1 download_atac_filtered_bams.txt 
rename x0 x x* 
rename x0 x x* 
rename x0 x x* 
rename x x0 
chmod +x x*

./sbatch.sh 

