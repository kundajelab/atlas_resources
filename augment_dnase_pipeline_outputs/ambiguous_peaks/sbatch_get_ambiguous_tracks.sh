#!/bin/bash
#idr_peak_files=/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/idr.optimal.narrowPeak
#overlap_peak_files=/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/overlap.optimal.narrowPeak
idr_peak_files=idr.optimal.narrowPeak
overlap_peak_files=overlap.optimal.narrowPeak
numlines=`cat $idr_peak_files |wc -l`
for i in `seq 1 $numlines`
do
    idr_peaks=`head -n$i $idr_peak_files | tail -n1`
    overlap_peaks=`head -n$i $overlap_peak_files | tail -n1`
    jobname=`basename $idr_peaks`
    sbatch -J $jobname -e logs/$jobname.$i.e -o logs/$jobname.$i.o -p euan,akundaje,owners,normal get_ambiguous_tracks.sh $idr_peaks $overlap_peaks 
done
