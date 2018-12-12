for suffix in ['train','validate','test']:
    data=open('gecco_v2.'+suffix+'.bed','r').read().strip().split('\n')
    outf=open('gecco_v2.'+suffix+'.200center.bed','w')
    count=0 
    for line in data[1::]:
        tokens=line.split('\t')
        chrom=tokens[0]
        startval=int(tokens[1])
        endval=int(tokens[2])
        middle=startval+(endval-startval)/2
        startval_centered=middle-100
        endval_centered=middle+100
        outf.write(chrom+'\t'+str(int(startval_centered))+'\t'+str(int(endval_centered))+'\t'+str(count)+'\n')
        count+=1
