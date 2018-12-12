import argparse

def parse_args():
        parser=argparse.ArgumentParser(description="Provide a gappedPeak file")
        parser.add_argument("--i",help="input bed file in format of chrom start_pos end_pos")
        parser.add_argument("--o",help="output bed track file")
        return parser.parse_args()

def main():
    args=parse_args()
    data=open(args.i,'r').read().strip().split('\n')
    outf=open(args.o,'w')
    counter=0 
    for line in data:
        tokens=line.split('\t')[0:3]
        outf.write('\t'.join(tokens)+'\t'+str(counter)+'\t'+str(counter)+'\t.\n')
        counter+=1
    
        
if __name__=="__main__":
    main()
