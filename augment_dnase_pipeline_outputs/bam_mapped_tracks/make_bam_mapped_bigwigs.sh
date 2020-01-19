#!/bin/bash 
cur_bam=$1
#source activate encode-atac-seq-pipeline 
bamCoverage -p16 -v --samFlagExclude 4 -b $cur_bam -o $cur_bam.bw
