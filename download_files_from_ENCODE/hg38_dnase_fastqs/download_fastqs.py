#intersects the experiments.tsv and files.tsv metadata files to determine fastq files to aggregate for a given experiment 
import pandas as pd 
import numpy as np 
import os 
import argparse 
import subprocess 
import multiprocessing.Threads 

def parse_args(): 
    parser=argparse.ArgumentParser(description="intersects the experiments.tsv and files.tsv metadata files to determine fastq files to aggregate for a given experiment")
    parser.add_argument("--experiments_metadata")
    parser.add_argument("--files_metadata") 
    parser.add_argument("--out_dir") 
    parser.add_argument("--threads",type=int,default=1) 
    return parser.parse_args() 

def download_experiment(inputs):
    experiment=inputs[0] 
    out_dir=inputs[1]
    contributing_files=inputs[2] 

    experiment_stripped=experiment.strip('/').split('/')[-1] 
    print("processing:"+str(experiment_stripped))
    outf='/'.join([out_dir,experiment_stripped+'.fastq.gz'])
    if os.path.exists(outf): 
        if args.overwrite==False: 
            return "done!"
            #the aggregted fastq for experiment already exists, skipping
        else: 
            print("warning! you are overwriting:"+outf)
    for index,row in contributing_files.iterrows(): 
        #get the file url 
        cur_url="https://www.encodeproject.org"+row['Download URL']
        #append the contents of the fastq.gz file to existing output file 
        completed_download=subprocess.run(['curl',curl_url,'>>',outf])
        completed_download.check_returncode()
    print("done!") 
    return "done!" 

def main(): 
    args=parse_args() 
    experiments=pd.read_csv(args.experiments_metadata,header=0,sep='\t',skiprows=1,index_col=['ID']) 
    files=pd.read_csv(args.files_metadata,header=0,sep='\t',skiprows=1,index_col=['ID']) 
    print("loaded files and experiments metadata") 
    
    #if the output directory for bam storage does not exist, create it 
    if not os.path.exists(args.out_dir): 
        os.makedirs(args.outdir)     
    #create sub-directories for unfiltered alignments and alignments (which may also be unfiltered and are used if no unfiltered alignments are specified) 
    if not os.path.exists('/'.join([args.out_dir,'unfiltered_alignments'])): 
        os.makedirs('/'.join([args.out_dir,'unfiltered_alignments']))
    if not os.path.exists('/'.join([args.out_dir,'alignments'])): 
        os.makedirs('/'.join([args.out_dir,'alignments']))
    print("verified that output directories exist, created if needed") 

    #subset the bam files to the ones in the experiment list
    experiments_to_use=np.asarray(experiments.index)
    pool=ThreadPool(args.threads)
    pool_args=[] 
    for experiment in experiments_to_use: 
        contributing_files=files[files['Dataset']==experiment]
        pool_args.append([experiment,args.out_dir,contributing_files])

    downloads=pool.map(download_experiment,pool_args) 
    pool.close()
    pool.join() 

if __name__=="__main__": 
    main() 
