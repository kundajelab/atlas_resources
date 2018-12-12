# add positive or negative labels to subset beds, combine them into a single file 
import argparse
import pandas as pd 
def parse_args():
    parser=argparse.ArgumentParser(description="add positive or negative labels to subset beds, comine them into a single file")
    parser.add_argument("--bed",nargs="+")
    parser.add_argument("--labels",nargs="+")
    parser.add_argument("--ntasks",type=int,default=1)
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args()
    outf=open(args.outf,'w')
    for i in range(len(args.bed)):
        data=open(args.bed[i],'r').read().strip().split('\n')
        cur_label=args.labels[i]
        for line in data:
            outf.write(line+args.ntasks*('\t'+str(cur_label))+'\n')

if __name__=="__main__":
    main()
    
