#generates dinucleotide frequencies for a bed file
import argparse
from change_negs import *
import pysam
import pandas as pd
import pdb 
def parse_args():
    parser=argparse.ArgumentParser(description="generate dinucleotide frequencies for a bed file")
    parser.add_argument("--bed_path")
    parser.add_argument("--ratio_neg_to_pos",nargs="+",type=float)
    parser.add_argument("--outf")
    parser.add_argument("--ref_fasta")
    parser.add_argument("--dinuc_freqs",default=None)
    parser.add_argument("--task",type=int,default=None)
    parser.add_argument("--gc",action="store_true")
    parser.add_argument("--header",action="store_true")
    
    return parser.parse_args()

def get_balanced_negative(args):
    header=None
    if args.header==True:
        header=0 
    data=pd.read_csv(args.bed_path,header=None,sep='\t',index_col=[0,1,2])
    print(data.shape)
    n_to_skip=0
    if args.header==True:
        n_to_skip=1
    freqs=np.loadtxt(args.dinuc_freqs,skiprows=n_to_skip)
    print(freqs.shape) 
    if args.task!=None:
        if args.gc==True:
            negs_gcmatched_samp(data.iloc[:,args.task],freqs,args.ratio_neg_to_pos[args.task],args.outf+'.'+str(args.task))
        else:
            negs_dinucmatched_samp(data.iloc[:,args.task],freqs,args.ratio_neg_to_pos[args.task],args.outf+'.'+str(args.task))
    else:
        numtasks=data.shape[1]
        for task in range(numtasks):
            if args.gc==True:
                negs_gcmatched_samp(data.iloc[:,task],freqs,args.rato_neg_to_pos[task],args.outf+'.'+str(task))
            else: 
                negs_dinucmatched_samp(data.iloc[:,task],freqs,args.ratio_neg_to_pos[task],args.outf+'.'+str(task))
            print("generated negatives for task:"+str(task))    

def get_gc_mat(args):
    #open the reference file
    ref=pysam.FastaFile(args.ref_fasta)
    #load the train data as a pandas dataframe, skip the header
    data=pd.DataFrame.from_csv(args.bed_path,header=None,sep='\t',index_col=[0,1,2])
    bed_entries=[i for i in data.index]
    print("got the bed entries")
    cur_entry=0
    outf=open(args.outf,'w')
    for entry in bed_entries:
        seq=ref.fetch(entry[0],entry[1],entry[2]).upper()
        gc_fract=(seq.count('G')+seq.count('C'))/float(len(seq))
        outf.write(str(gc_fract)+'\n')
    
            
def get_dinuc_mat(args):
    #open the reference file
    ref=pysam.FastaFile(args.ref_fasta)
    #load the train data as a pandas dataframe, skip the header
    data=pd.DataFrame.from_csv(args.bed_path,header=0,sep='\t',index_col=[0,1,2])
    bed_entries=[i for i in data.index]
    print("got the bed entries")
    freq_dict=dict()
    all_dinucs=['AA','AC','AG','AT','CA','CC','CG','CT','GA','GC','GG','GT','TA','TC','TG','TT']
    for dinuc in all_dinucs:
        freq_dict[dinuc]=dict()
    cur_entry=0 
    for entry in bed_entries:
        seq=ref.fetch(entry[0],entry[1],entry[2]).upper()
        for k in freq_dict.keys():
            freq_dict[k][cur_entry]=0.0
        #get the dinucleotide frequencies
        for ind in range(999):
            try:
                freq_dict[seq[ind:ind+2]][cur_entry]+=1
            except:
                print(seq[ind:ind+2])
        cur_entry+=1
        if (cur_entry % 1000==0):
            print(str(cur_entry))
    print("got dinuc counts")
    outf=open(args.outf,'w')
    outf.write('\t'.join(all_dinucs)+'\n')
    for i in range(cur_entry):
        fract=[str(freq_dict[d][i]/1000) for d in all_dinucs]
        outf.write('\t'.join(fract)+'\n')
            
def main():
    
    args=parse_args()
    if args.dinuc_freqs==None:
        #generate and save the dinucleotide frequency matrix
        if args.gc==True:
            get_gc_mat(args)
        else: 
            get_dinuc_mat(args)
    #else:
    #    #generate di-nucleotide-balanced negative sets
    get_balanced_negative(args)
        
        
    
if __name__=="__main__":
    main()
    
    
    
    
