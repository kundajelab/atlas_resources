import pandas as pd 
import argparse
import json
import os
from os import path, listdir
from os.path import isfile, join

def parse_args(): 
    parser=argparse.ArgumentParser(description="generate pipeline input jsons")
    parser.add_argument("--fastq_dir") 
    parser.add_argument("--pipeline_json_dir")
    parser.add_argument("--pipeline_output_dir") 
    parser.add_argument("--caper_submit_script")
    parser.add_argument("--genome_tsv_for_pipeline",default="/home/groups/cherry/encode/pipeline_genome_data/hg38_sherlock.tsv")
    return parser.parse_args() 

def main(): 
    args=parse_args() 

    #create the pipeline_json_dir if it doesn't exist yet, this is where all the jsons for the pipeline will be stored.
    if os.path.exists(args.pipeline_json_dir) is False:
        os.makedirs(args.pipeline_json_dir)

    if os.path.exists(args.pipeline_output_dir) is False:
        os.makedirs(args.pipeline_output_dir)

    print("ensured that directories for input jsons and pipeline outputs exist")
    fastq_files = [f for f in listdir(args.fastq_dir) if isfile(join(args.fastq_dir, f))]
    sample_to_json=dict() 
    for f in fastq_files:
        #create the input json for the current fastq file
        if f.endswith('.fastq.gz'):
            sample=f.replace('.fastq.gz','')
            f_full_path='/'.join([args.fastq_dir,f])
            json_path='/'.join([args.pipeline_json_dir,sample])+'.json'
            cur_json_dict={}
            cur_json_dict['atac.pipeline_type']="dnase"
            cur_json_dict['atac.genome_tsv']=args.genome_tsv_for_pipeline
            cur_json_dict['atac.fastqs_rep1_R1']=[f_full_path]
            cur_json_dict['atac.paired_ends']=[False]
            cur_json_dict['atac.enable_idr']=True
            cur_json_dict['atac.idr_thresh']=0.05
            cur_json_dict['atac.bowtie2_cpu']=8
            cur_json_dict['atac.filter_cpu']=8
            cur_json_dict['atac.bam2ta_cpu']=8
            cur_json_dict['atac.xcor_cpu']=8
            with open('/'.join([args.pipeline_json_dir,'.'.join([sample,'json'])]),'w') as json_outf:
                json.dump(cur_json_dict,json_outf)
            #create the output directory for pipeline outputs for the current sample
            if os.path.exists(json_path) is False:
                os.makedirs(json_path)
            #add entry to sample_to_json dict for use in creating run script for pipeline submission
            sample_to_json[sample]=json_path
            
    #create the caper submit script
    with open(args.caper_submit_script,'w') as submit_f:
        submit_f.write('#!/bin/bash\n')
        submit_f.write('source activate encode-atac-seq-pipeline\n')
        for sample in sample_to_json:
            submit_f.write('caper submit /home/users/annashch/atac-seq-pipeline/atac.wdl -i '+sample_to_json[sample]+' -s '+sample+' --ip $1 --port 8000\n')
    
    
            
if __name__=="__main__": 
    main() 

