#!/bin/bash 
#tagAligns=/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/merged.nodup.tagAligns.txt
tagAligns=merged.nodup.tagAligns.txt
for f in `cat $tagAligns`
do
    jobname=`basename $f`
    sbatch -J $jobname -e logs/$jobname.e -o logs/$jobname.o -p akundaje,euan,owners --mem 10000  make_count_tracks.sh $f
done

