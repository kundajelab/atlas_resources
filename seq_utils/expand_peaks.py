#threshold a narrowPeak file to a region of a specified size around the summit.
import argparse
import math

def parse_args():
    parser=argparse.ArgumentParser(description="expand peak to desired length")
    parser.add_argument("--bed_file")
    parser.add_argument("--target_length",type=int,default=1000) 
    parser.add_argument("--outf")
    parser.add_argument("--skip_header",action="store_true")
    return parser.parse_args()

def main():
    args=parse_args()
    outf=open(args.outf,'w')
    bed_file=open(args.bed_file,'r').read().strip().split('\n')
    starting_index=0
    if (args.skip_header==True):
        starting_index=1
        outf.write(bed_file[0]+'\n')
    for line in bed_file[starting_index::]:
        tokens=line.split('\t')
        chrom=tokens[0]
        start_pos=int(tokens[1])
        end_pos=int(tokens[2])
        padding=args.target_length - (end_pos - start_pos)
        left_pad=math.floor(padding/2)
        right_pad=math.ceil(padding/2)
        new_start=start_pos-left_pad
        new_end=end_pos+right_pad
        other='\t'.join(tokens[3::])
        outf.write(chrom+'\t'+str(new_start)+'\t'+str(new_end)+'\t'+other+'\n')
        
        

if __name__=="__main__":
    main()
    
    

