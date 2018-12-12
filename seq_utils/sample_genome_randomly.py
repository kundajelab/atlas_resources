#randomly sample regions from a specified genome.
#This is useful for generating candidate negatives for training deep learning models
#The output bed file should be intersected with a specified positive set and then submitted to
#deeplearning/form_inputs/code/gc_dinuc_balanced
#(https://github.com/kundajelab/deeplearning/tree/annashch-branch/form_inputs/code/gc_dinuc_balanced)
import argparse
import random


def parse_args():
    parser=argparse.ArgumentParser(description="#randomly sample regions from a specified genome. This is useful for generating candidate negatives for training deep learning models The output bed file should be intersected with a specified positive set and then submitted to deeplearning/form_inputs/code/gc_dinuc_balanced (https://github.com/kundajelab/deeplearning/tree/annashch-branch/form_inputs/code/gc_dinuc_balanced)")
    parser.add_argument("--chrom_sizes",default="/mnt/data/annotations/by_release/hg19.GRCh37/hg19.chrom.sizes")
    parser.add_argument("--region_size",type=int,default=1000)
    parser.add_argument("--region_n",type=int,default=1000000)
    parser.add_argument("--outf")
    parser.add_argument("--main_chroms_only",action="store_true")
    return parser.parse_args()

def main():
    args=parse_args()
    outf=open(args.outf,'w')
    chrom_sizes=open(args.chrom_sizes,'r').read().strip().split('\n')
    chrom_size_dict=dict()
    for line in chrom_sizes:
        tokens=line.split('\t')
        if args.main_chroms_only==True:
            if tokens[0].__contains__('_'):
                continue
        chrom_size_dict[tokens[0]]=int(tokens[1])

    #The probability of selecting a region from a chromosome should reflect the size of the chromosome. 
    total_size=sum(list(chrom_size_dict.values()))
    thresholds=[]
    chroms=[] 
    thresh=0
    for cur_chrom in chrom_size_dict:
        cur_chrom_size_fraction=chrom_size_dict[cur_chrom]/total_size
        print("cur_chrom_size_fraction:"+str(cur_chrom_size_fraction))
        cur_chrom_thresh=thresh+cur_chrom_size_fraction
        chroms.append(cur_chrom)
        thresholds.append(cur_chrom_thresh)
        thresh=cur_chrom_thresh      
    num_chroms=len(chroms)
    print(thresholds)
    print(chroms) 
    num_sampled=0
    while num_sampled < args.region_n:
        #sample a region
        
        #randomly select a chromosome
        selector=random.random()
        for i in range(num_chroms):
            if selector <= thresholds[i]:
                cur_chrom=chroms[i]
                break
        #select a region on the chromosome
        start_pos=random.randint(1,chrom_size_dict[cur_chrom]-args.region_size)
        end_pos=start_pos+args.region_size
        outf.write(cur_chrom+'\t'+str(start_pos)+'\t'+str(end_pos)+'\n')
        num_sampled+=1
        if num_sampled%1000==0:
            print(num_sampled)
        
if __name__=="__main__":
    main()
    
