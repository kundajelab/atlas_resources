#randomly sample a given number of regions from a bed file
import argparse
import pandas as pd
import pdb
def parse_args():
    parser=argparse.ArgumentParser(description="randomly sample a given number of regions from a bed file")
    parser.add_argument("--bed")
    parser.add_argument("--n",type=int,default=None,help="omit this argument if you just want to shuffle the entire file")
    parser.add_argument("--outf",default=None)
    parser.add_argument("--header",action="store_true",default=False) 
    return parser.parse_args()

def main():
    args=parse_args()
    if (args.header==False):
        bed=pd.read_csv(args.bed,sep='\t',header=None)
    else:
        bed=pd.read_csv(args.bed,sep='\t',header=0)
    if args.n==None:
        #select all regions from the bed file and shuffle them
        n=bed.shape[0]
    else:
        n=args.n
    sampled=bed.sample(n)
    if (args.header==False):
        sampled.to_csv(args.outf,sep='\t',index=False,header=False)
    else:
        sampled.to_csv(args.outf,sep='\t',index=False,header=True)
if __name__=="__main__":
    main()
    
