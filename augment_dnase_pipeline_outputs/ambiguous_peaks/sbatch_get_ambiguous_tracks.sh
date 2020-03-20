#!/bin/bash
#idr_peak_files=/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/idr.optimal.narrowPeak
#overlap_peak_files=/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/overlap.optimal.narrowPeak
idr_peak_files=idr.optimal.narrowPeak
overlap_peak_files=overlap.optimal.narrowPeak
numlines=`cat $idr_peak_files |wc -l`
for i in 1 `seq 1 $numlines`
do
    idr_peaks=`head -n$i $idr_peak_files | tail -n1`
    overlap_peaks=`head -n$i $overlap_peak_files | tail -n1`
    jobname=`basename $idr_peaks`
    sbatch -J $jobname -e logs/$jobname.e -o logs/$jobname.o -p euan,akundaje,owners get_ambiguous_tracks.sh $idr_peaks $overlap_peaks 
    #./get_ambiguous_tracks.sh $idr_peaks $overlap_peaks 
done
