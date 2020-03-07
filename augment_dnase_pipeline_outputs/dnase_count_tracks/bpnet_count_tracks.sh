#!/bin/bash 
cur_bam=$1
#source activate encode-atac-seq-pipeline 
bamCoverage -p16 -v --binSize 1 --samFlagExclude 780 --Offset 1 2 --minMappingQuality 30 -b $cur_bam -o $cur_bam.bpnet.bw
