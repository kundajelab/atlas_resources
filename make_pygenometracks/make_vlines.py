outf=open("vlines.old.bed",'w')
data=open("hg38.blacklist.bed",'r').read().strip().split('\n')
for line in data:
    tokens=line.split('\t')
    chrom=tokens[0]
    start=int(tokens[1])
    end=int(tokens[2])
    outf.write(chrom+'\t'+str(start)+'\t'+str(start+1)+'\n')
    outf.write(chrom+'\t'+str(end)+'\t'+str(end+1)+'\n')
outf.close()

outf=open("vlines.new.bed",'w')
data=open("hg38-blacklist.v2.bed",'r').read().strip().split('\n')
for line in data:
    tokens=line.split('\t')
    chrom=tokens[0]
    start=int(tokens[1])
    end=int(tokens[2])
    outf.write(chrom+'\t'+str(start)+'\t'+str(start+1)+'\n')
    outf.write(chrom+'\t'+str(end)+'\t'+str(end+1)+'\n')
outf.close()
outf=open("vlines.peakPass.bed",'w')
data=open("peakPass60Perc_sorted.bed",'r').read().strip().split('\n')
for line in data:
    tokens=line.split('\t')
    chrom=tokens[0]
    start=int(tokens[1])
    end=int(tokens[2])
    outf.write(chrom+'\t'+str(start)+'\t'+str(start+1)+'\n')
    outf.write(chrom+'\t'+str(end)+'\t'+str(end+1)+'\n')
outf.close()

    
