import argparse
import pybedtools
from pybedtools import BedTool
import pandas as pd
import numpy as np 
import pdb
import csv

def parse_args():
    parser=argparse.ArgumentParser("generated task-specific negatives for a multi-tasked input matrix")
    parser.add_argument("--task_list",help="this is a tab-separated file with the name of the task in the first column and the path to the corresponding bed file in the second column")
    parser.add_argument("--outf")
    parser.add_argument("--training_bin_size",type=int,default=1000)
    parser.add_argument("--chromsizes") 
    return parser.parse_args()

def write_outputs(args,label_dict,size_corrected_master_bed):
    #faster to write in a single operation as a pandas df
    print("writing output file")
    tasks=list(label_dict.keys())
    num_tasks=len(tasks)
    num_entries=len(size_corrected_master_bed)
    data_for_np=np.zeros((num_entries,num_tasks))
    for i in range(num_tasks):
        cur_task=tasks[i]
        data_for_np[:,i]=label_dict[cur_task]
    data=pd.DataFrame(data=data_for_np,
                      index=[str(i).strip('\n') for i in size_corrected_master_bed],
                      columns=tasks)
    data.to_csv(args.outf,sep='\t',index_label="Chrom\tStart\tEnd")

def get_labels(task_bedfiles,size_corrected_master_bed,training_bin_size):
    print("getting labels")
    label_dict=dict()
    for task in task_bedfiles:
        print(task) 
        labels=[]
        processed=dict()
        try:
            intersection=size_corrected_master_bed.intersect(task_bedfiles[task],wao=True)
        except:
            continue 
        for entry in intersection:
            overlap=int(entry[-1])
            master_peak='\t'.join(entry[0:3])
            if master_peak in processed:
                continue
            processed[master_peak]=1
            #if there is no overlap with the task bed file, the label is 0 
            if overlap==0:
                labels.append(0)
            else:
                summit_offset=int(entry[-2])
                peak_start=int(entry[4])
                peak_end=int(entry[5])
                if summit_offset!=-1:
                    #check to see if the summit falls in the master_peak
                    summit=int(entry[4])+summit_offset
                    master_peak_start=int(entry[1])
                    master_peak_end=int(entry[2])
                    if (master_peak_start <= summit <= master_peak_end):
                        labels.append(1)
                    else:
                        labels.append(-1)
                else:
                    task_peak_size=peak_end-peak_start
                    tocheck=min([task_peak_size,training_bin_size])
                    if overlap/tocheck > 0.5:
                        #it's a positive, more than 1/2 the task peak overlaps with master bed region (or vice versa)
                        labels.append(1)
                    else:
                        #ambiguous, exclude from analysis
                        labels.append(-1)
        label_dict[task]=labels        
    print("got labels") 
    return label_dict


def size_correct(master_bed,bin_size,chromsizes):
    chromsizes=open(chromsizes,'r').read().strip().split('\n')
    chromsize_dict=dict()
    for line in chromsizes:
        tokens=line.split('\t')
        chromsize_dict[tokens[0]]=int(tokens[1])
    corrected_master_bed=[]
    for entry in master_bed:
        chrom=entry[0] 
        entry_start=int(entry[1])
        entry_end=int(entry[2]) 
        cur_size=entry_end-entry_start
        
        if(cur_size > bin_size):
            #truncate the entry to the specified bin size 
            overhang=(cur_size-bin_size)/2
            entry_start=entry_start+overhang
            entry_end=entry_end-overhang
            new_size=entry_end-entry_start
            assert (new_size==bin_size)
            
        elif(cur_size < bin_size):
            #pad the entry to the specified bin size 
            padding=(bin_size-cur_size)/2
            entry_start=entry_start-padding
            entry_end=entry_end+padding
            new_size=entry_end-entry_start
            assert new_size==bin_size
        if entry_start <1:
            entry_start=1
            entry_end=entry_start+bin_size
        if (entry_end <= chromsize_dict[chrom]):
            corrected_master_bed.append('\t'.join([str(i) for i in [chrom,int(entry_start),int(entry_end)]]))
        
    #convert to a BedTool
    corrected_master_bed=BedTool('\n'.join(corrected_master_bed),from_string=True)
    return corrected_master_bed


def load_bed_files_for_tasks(tasks): 
    task_bedfiles=dict()
    #concatenate bed files to create a single master list 
    master_bed=None
    for index,row in tasks.iterrows():
        #pdb.set_trace() 
        taskname=row['Task']
        print(taskname)
        cur_bed=BedTool(row['File'])
        if master_bed==None:
            master_bed=cur_bed
        else:
            master_bed=master_bed.cat(cur_bed)
        task_bedfiles[taskname]=cur_bed
    print("loaded bed files for all tasks")
    return task_bedfiles,master_bed

def main():
    args=parse_args()
    tasks=pd.read_csv(args.task_list,sep='\t',header=0)
    
    #load the task bed files and generate a master bed file 
    task_bedfiles,master_bed=load_bed_files_for_tasks(tasks)
    
    #generate specified size regions from the master bed file (i.e. 1kb or 2kb)
    size_corrected_master_bed=size_correct(master_bed,args.training_bin_size,args.chromsizes)

    #generate labels for each task
    label_dict=get_labels(task_bedfiles,size_corrected_master_bed,args.training_bin_size)

    #write the labels to output file 
    write_outputs(args, label_dict,size_corrected_master_bed)
    
        
    

if __name__=="__main__":
    main()
    
    
