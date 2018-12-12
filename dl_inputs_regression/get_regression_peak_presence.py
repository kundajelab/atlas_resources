import numpy as np 
data=open('../counts_merged.txt','r').read().strip().split('\n') 
header=open('../counts_merged.metadata','r').read().strip().split('\n') 
header_dict=dict() 
for i in range(len(header)): 
    header_dict[i]=header[i].split('_')[0]  
header_keys=header_dict.keys()
header_keys.sort() 
header_vals=[header_dict[k] for k in header_keys]  
header_vals=list(set(header_vals))
header_vals.sort() 
count_dict=dict() 
outf=open('peak_presence_regression.txt','w') 
outf.write('Peak\t'+'\t'.join(header_vals)+'\n')
j=0 
for line in data: 
    tokens=line.split('\t') 
    tokens=[float(i) for i in tokens] 
    count_dict[j]=dict() 
    for i in range(len(tokens)): 
        headerval=header_dict[i] 
        if headerval not in count_dict[j]:
            count_dict[j][headerval]=[tokens[i]] 
        else: 
            count_dict[j][headerval].append(tokens[i])
    j+=1
for k in range(j): 
    outf.write(str(k))
    for headerval in header_vals: 
        curvals=count_dict[k][headerval]
        averaged=sum(curvals)/float(len(curvals))        
        outf.write('\t'+str(averaged))
    outf.write('\n') 

        
        
