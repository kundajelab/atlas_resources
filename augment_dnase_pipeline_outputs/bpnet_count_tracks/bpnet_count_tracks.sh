#!/bin/bash 
cur_bam=$1
#source activate encode-atac-seq-pipeline


#non-stranded (can be PE or SE) 
bamCoverage -p16 -v --binSize 1 --samFlagExclude 780 --Offset 1 1 --minMappingQuality 30 -b $cur_bam -o $cur_bam.bpnet.unstranded.bw

#forward strand -- assumes SE data
bamCoverage -p16 -v --binSize 1 --samFlagExclude 796 --Offset 1 1 --minMappingQuality 30 -b $cur_bam -o $cur_bam.bpnet.plus.bw

#reverse strand -- assumes SE data
bamCoverage -p16 -v --binSize 1 --samFlagExclude 780 --samFlagInclude 16 --Offset 1 1 --minMappingQuality 30 -b $cur_bam -o $cur_bam.bpnet.minus.bw
