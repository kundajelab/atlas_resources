#threshold a narrowPeak file to a region of a specified size around the summit.
import argparse
def parse_args():
    parser=argparse.ArgumentParser(description="Threshold a narrowPeak file to a region of a specified size around the summit.")
    parser.add_argument("--bed_file")
    parser.add_argument("--flank",help="flank to use for selecting region around summit",type=int,default=499)
    parser.add_argument("--target_length",type=int,default=1000) 
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args()
    outf=open(args.outf,'w')
    bed_file=open(args.bed_file,'r').read().strip().split('\n')
    flank=args.flank
    for line in bed_file:
        tokens=line.split('\t')
        chrom=tokens[0]
        start_pos=int(tokens[1])
        end_pos=int(tokens[2])
        summit_offset=int(tokens[-1])
        summit_pos=start_pos+summit_offset
        new_start=summit_pos-flank
        new_end=summit_pos+flank
        padding=args.target_length - (new_end-new_start)
        new_end=new_end+padding
        outf.write(chrom+'\t'+str(new_start)+'\t'+str(new_end)+'\n')
        
        

if __name__=="__main__":
    main()
    
    
