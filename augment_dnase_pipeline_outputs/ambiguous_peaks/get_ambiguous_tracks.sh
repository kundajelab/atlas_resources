#!/bin/bash
idr_peaks=$1
overlap_peaks=$2
/share/PI/euan/apps/bin/bedtools intersect -v -a $overlap_peaks -b $idr_peaks| bgzip -c  > $overlap_peaks.ambiguous.bed.gz 
