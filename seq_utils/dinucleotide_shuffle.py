#accepts a bed file as input, returns original fasta & dinucleotide-shuffled fasta as output
import argparse
import pysam
import random
def parse_args():
    parser=argparse.ArgumentParser(description="accepts a bed file as input, returns original fasta & dinucleotide-shuffled fasta as output")
    parser.add_argument("--input_bed")
    parser.add_argument("--output_prefix")
    parser.add_argument("--ref_fasta",default="/srv/scratch/annashch/deeplearning/form_inputs/code/hg19.genome.fa")
    parser.add_argument("--imbalance",type=int,default=1)
    return parser.parse_args()


def shuffle(seq):
    #get list of dinucleotides
    nucs=[]
    for i in range(0,len(seq),2):
        nucs.append(seq[i:i+2])
    #generate a random permutation
    random.shuffle(nucs)
    return ''.join(nucs) 
    
def main():
    args=parse_args()
    #open the reference for reading
    ref=pysam.FastaFile(args.ref_fasta)
    outf=open(args.output_prefix+".dinucshuffled.negatives.fasta",'w')
    source_bed=open(args.input_bed,'r').read().strip().split('\n')
    index=0 
    for line in source_bed:
        tokens=line.split('\t')
        if tokens[-1]!="1":
            #we only want the positives 
            continue
        seq=ref.fetch(tokens[0],int(tokens[1]),int(tokens[2]))
        outf.write('>'+str(index)+';'+'label=1\n')
        outf.write(seq+'\n')
        index+=1
        for i in range(args.imbalance):
            #perform dinucleotide shuffling
            shuffled=shuffle(seq)
            outf.write('>'+str(index)+';'+'label=0\n')
            outf.write(shuffled+'\n')
            index+=1

        
if __name__=="__main__":
    main()
    
