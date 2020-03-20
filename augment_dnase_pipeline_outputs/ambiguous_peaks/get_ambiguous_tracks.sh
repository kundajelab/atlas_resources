#!/bin/bash
idr_peaks=$1
overlap_peaks=$2
bedtools intersect -v -a $overlap_peaks -b $idr_peaks | cut -f1,2,3 > $overlap_peaks.ambiguous.bed
cut -f1,2,3 ../../make_pygenometracks/all_three_blacklists.bed >> $overlap_peaks.ambiguous.bed
bedtools sort -i $overlap_peaks.ambiguous.bed > $overlap_peaks.ambiguous.bed.tmp
mv $overlap_peaks.ambiguous.bed.tmp $overlap_peaks.ambiguous.bed
bgzip -f $overlap_peaks.ambiguous.bed

