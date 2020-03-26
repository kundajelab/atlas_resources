#!/bin/bash 
bams=bowtie2_bams.txt
#bams=tier1.bowtie2_bams.txt
for f in `cat $bams`
do
    jobname=`basename $f`
    sbatch -J $jobname.plus -e logs/$jobname.plus.e -o logs/$jobname.plus.o -p akundaje,euan,owners --time=500 -N1 -n16 bpnet_count_tracks.sh $f
done

