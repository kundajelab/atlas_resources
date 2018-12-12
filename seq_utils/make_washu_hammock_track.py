import argparse

def parse_args():
        parser=argparse.ArgumentParser(description="Provide a bed file to color-code by label (0,1,-1)")
        parser.add_argument("--i",help="input bed file in format of chrom start_pos end_pos label")
        return parser.parse_args()

def main():
    args=parse_args()
    data=open(args.i,'r').read().strip().split('\n')
    outf=open(args.i+'.hammock','w')
    counter=0 
    for line in data:
        tokens=line.split('\t')
        if tokens[-1]=='-1':
                tokens[-1]='2'
        tokens[-1]='category:'+tokens[-1]+',id:'+str(counter)
        outf.write('\t'.join(tokens)+'\n')
        counter+=1
    
        
if __name__=="__main__":
    main()
