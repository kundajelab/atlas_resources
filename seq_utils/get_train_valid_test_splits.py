#split a bed file into training, validation, test sets by specifying chromosomes to use in each
import argparse
def parse_args():
    parser=argparse.ArgumentParser(description="split a bed file into training, validation, test sets by specifying chromosomes to use in each")
    parser.add_argument("--source")
    parser.add_argument("--test_chroms",nargs="+")
    parser.add_argument("--valid_chroms",nargs="+")
    parser.add_argument("--out_prefix")
    return parser.parse_args()

def main():
    args=parse_args()
    
    outf_train=open(args.out_prefix+".train.bed",'w')
    outf_test=open(args.out_prefix+".test.bed",'w')
    outf_validate=open(args.out_prefix+".validate.bed",'w')

    data=open(args.source,'r').read().strip().split('\n')
    header=data[0]
    
    outf_train.write(header+'\n')
    outf_test.write(header+'\n')
    outf_validate.write(header+'\n')

    test_chroms=dict()
    for c in args.test_chroms:
        test_chroms[c]=1
    valid_chroms=dict()
    for c in args.valid_chroms:
        valid_chroms[c]=1

    for line in data[1::]:
        tokens=line.split('\t')
        chrom=tokens[0]
        if chrom in test_chroms:
            outf_test.write(line+'\n')
        elif chrom in valid_chroms:
            outf_validate.write(line+'\n')
        else:
            outf_train.write(line+'\n')
            

if __name__=="__main__":
    main()
    
    
