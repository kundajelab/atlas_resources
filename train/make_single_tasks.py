data=open('encode.dnase.tasks.tsv','r').read().strip().split('\n')
for line in data:
    task=line.split('/')[-1]
    outf=open(task+'.task.tsv','w')
    outf.write(line+'\n')
    outf.close()
    
