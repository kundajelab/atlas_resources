import argparse
from pybedtools import BedTool
import pandas as pd
import numpy as np 
import pdb
import csv
from classification_label_protocols import * 
from multiprocessing.pool import ThreadPool


#Approaches to determining classification labels
#Others can be added here (imported from classification_label_protocols) 
labeling_approaches={
    "peak_summit_near_bin_center":peak_summit_near_bin_center,
    "peak_percent_overlap_with_bin":peak_percent_overlap_with_bin
    }

def parse_args():
    parser=argparse.ArgumentParser(description="Generate genome-wide labeled bins for a set of narrowPeak task files ")
    parser.add_argument("--task_list",help="this is a tab-separated file with the name of the task in the first column and the path to the corresponding narrowPeak(.gz) file in the second column")
    parser.add_argument("--out_bed",help="output filename that labeled bed file will be saved to.")
    paresr.add_argument("--chrom_sizes",help="chromsizes file for the reference genome. First column is chrom name; second column is chrom size")
    parser.add_argument("--stride",type=int,default=50,help="stride to shift adjacent bins by")
    parser.add_argument("--bin_size",type=int,default=1000,help="bin length for input to model training")
    parser.add_argument("--bin_center_size",type=int,default=200,help="flank around bin center where peak summit falls in a positivei bin")
    parser.add_argument("--threads",type=int,default=1)
    parser.add_argument("--overlap_thresh",type=float,default=0.5,help="minimum percent of bin that must overlap a peak for a positive label")
    parser.add_argument("--allow_ambiguous",default=False,action="store_true")
    parser.add_argument("--labeling_approach",choices=["peak_summit_near_bin_center","peak_percent_overlap_with_bin"])    
    return parser.parse_args()

def get_labels_one_task(task_name,task_bed,args,non_zero_bins):
    #determine the appropriate labeling approach
    return labeling_approaches[args.labeling_approach](task_name,task_bed,args,non_zero_bins)
    

def write_output_bed(args,task_names,non_zero_bins):
    '''
    Generate output file 
    args - arguments that were passed to the main script 
    non_zero_bins - dictionary of the form tuple(chrom,start_bin,end_bin)->task_name->label 
    task_names - list of unique task names 
    '''
    #open the output file and write the header 
    outf=open(args.out_bed,'w')
    header='\t'.join(['\t'.join(['Chrom','Start','End']),
                      '\t'.join(tasks)])
    outf.write(header+'\n')

    #load the chromosome sizes 
    chrom_sizes=pd.read_table(args.chrom_sizes,header=None,sep='\t')
    print("loaded chrom_sizes")
    
    num_tasks=len(task_names)
    #iterate through each bin in the genome 
    for index,row in chrom_sizes.iterrows():
        chrom=row[0]
        chrom_size=row[1]
        
        print("Writing output file entries for chrom:"+str(chrom))
        for bin_start in range(1,chrom_size-args.bin_size,args.stride):
            
            #store the current bin as a tuple
            bin_end=bin_start+args.bin_size
            cur_bin=tuple(chrom,bin_start,bin_end)
            if cur_bin not in non_zero_bins:
                
                #all tasks have 0 label
                outf.write('\t'.join([str(i) for i in cur_bin])+
                           '\t'.join(['0']*num_tasks)+'\n')
            else:
                outf.write('\t'.join([str(i) for i in cur_bin]))
                #iterate through tasks to determine appropriate labels
                for task_name in task_names:
                    if task_name in non_zero_bins[cur_bin]:
                        outf.write('\t'+str(non_zero_bins[cur_bin][task_name]))
                    else:
                        outf.write('\t0')
                outf.write('\n')

def get_nonzero_bins(args,tasks):
    #parallelized bin labeling
    pool=ThreadPool(args.threads)
    if args.allow_ambiguous==True:
        print(' '.join(["determining positive and ambiguous bins with", args.threads, "threads"]))
    else:
        print(' '.join(["determining positive bins with",args.threads,"threads"]))
              
    #create dictionary to store non-zero bin labels of the form:
    # tuple(chrom,bin_start,bin_end)-> task->label
    non_zero_bins=dict()

    #keep track of all task names
    task_names=[]
    for task in tasks.iterrows():
        task_name=task[0]
        task_names.append(task_name)
        task_bed=BedTool(row[1])
        #get non-zero bin labels for the current task 
        pool.apply_async(get_labels_one_task,args=(task_name,task_bed,args,non_zero_bins))        
    pool.close()
    pool.join()
    print("finished parsing and labeling task bed files")
    return task_names,non_zero_bins

def main():
    
    #parse the input arguments
    args=parse_args()

    #read in the metadata file with task names in column 1 and path to peak file in column 2
    tasks=pd.read_csv(args.task_list,sep='\t',header=0)

    #multi-threaded identification of non-zero bin labels for each task 
    task_names,non_zero_bins=get_nonzero_bins(args,tasks) 

    #write the output file
    write_output_bed(args,task_names,non_zero_bins)
    

if __name__=="__main__":
    main()
    
    
