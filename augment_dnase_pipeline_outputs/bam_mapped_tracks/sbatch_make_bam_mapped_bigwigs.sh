#!/bin/bash 
for f in `cat /oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/bowtie2_bams`
do
    jobname=`basename $f`
    sbatch -c16 -J $jobname -e logs/$jobname.e -o logs/$jobname.o -p akundaje,euan,owners  make_bam_mapped_bigwigs.sh $f
done

