import pandas as pd
import argparse
def parse_args():
    parser=argparse.ArgumentParser(description="remove any bed regions greater than size of chromosomes")
    parser.add_argument("--chromsizes")
    parser.add_argument("--input_bed")
    parser.add_argument("--output_bed")
    parser.add_argument("--header",action="store_true")
    return parser.parse_args()

def main():
    args=parse_args()
    chromsize_data=open(args.chromsizes,'r').read().strip().split('\n')
    chromsize_dict=dict()
    for line in chromsize_data:
        tokens=line.split('\t')
        chromsize_dict[tokens[0]]=int(tokens[1])
    if args.header==True:
        data=pd.read_csv(args.input_bed,header=0,sep='\t')
    else:
        data=pd.read_csv(args.input_bed,header=None,sep='\t')
    outf=open(args.output_bed,'w')
    for index,row in data.iterrows():
        chrom=row[0]
        startpos=row[1]
        endpos=row[2]
        maxpos=chromsize_dict[chrom]
        if startpos > 0:
            if endpos < maxpos:
                outf.write('\t'.join([str(i) for i in row])+'\n')
            else:
                print(str(row))
        else:
            print(str(row))

if __name__=="__main__":
    main() 
