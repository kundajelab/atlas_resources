#!/bin/bash
#sed '1d' gecco.merged.inputs.dnase.onevall.universalneg.wholegenomeneg.bed > tmp
#python ~/anna_utils/seq_utils/make_washu_bed_track.py --i tmp --o tmp2
#rm tmp 
bedfile=tmp2
#tasks=(dnase_c dnase_v)
#bigwigs=("/oak/stanford/groups/akundaje/annashch/GECCO/DNase/processed/C_merged_bam/out/signal/macs2/rep1/C.trim.pf.fc.signal.bigwig" "/oak/stanford/groups/akundaje/annashch/GECCO/DNase/processed/V_merged_bam/out/signal/macs2/rep1/V_merged.trim.pf.fc.signal.bigwig")
#for((i=0;i<${#tasks[@]};i++))
#do
#    echo ${tasks[$i]}
#    echo ${bigwigs[$i]}
#    bigWigAverageOverBed -sampleAroundCenter=200 ${bigwigs[$i]} $bedfile ${tasks[$i]}.tab
#done
   
#python ../code/dl_inputs_regression/assemble_coverage.py --input_files dnase_c.tab dnase_v.tab \
#       --bed_file $bedfile \
#       --outf coverage.bed 
rm tmp2
python /srv/scratch/annashch/deeplearning/form_inputs/code/bed_utils/get_train_valid_test_splits.py --source coverage.bed \
       --valid_chroms chr18 chr19 chr20 \
       --test_chroms chr17 chr21 chr22 \
       --out_prefix gecco.merged.regression

