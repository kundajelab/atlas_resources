#!/bin/bash
prefix=$1 #everything except the .bam extension

#merge the true reps to get a merged bam (if you are not starting with a merged bam,  uncomment the line below)
#samtools merge $prefix.bam $2 $3 

#name sort to achieve random genomic pos
samtools sort -n --threads 50 -O bam -o $prefix.namesorted.bam $prefix.bam
echo "done sorting" 
samtools view -H $prefix.namesorted.bam > $prefix.pr1.sam
cp $prefix.pr1.sam $prefix.pr2.sam
echo "made headers"
sam1=$prefix.pr1.sam
sam2=$prefix.pr2.sam 
samtools view --threads 50  $prefix.namesorted.bam | awk -v sam1="$sam1" -v sam2="$sam2" '{if(NR%2){print >> sam1} else {print >> sam2}}'
samtools view -sB $sam1  | samtools sort -@50 -O bam -o $prefix.pr1.bam
samtools index $prefix.pr1.bam
samtools view -sB $sam2 | samtools sort -@50 -O bam -o $prefix.pr2.bam
samtools index $prefix.pr2.bam

#make bigwigs
bamCoverage -p50 -v --binSize 1 --samFlagExclude 780 --Offset 1 1 --minMappingQuality 30 -b $prefix.pr1.bam -o $prefix.pr1.unstranded.bw
bamCoverage -p50 -v --binSize 1 --samFlagExclude 780 --Offset 1 1 --minMappingQuality 30 -b $prefix.pr2.bam -o $prefix.pr2.unstranded.bw

