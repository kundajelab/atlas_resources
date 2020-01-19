idmap=open("processed_all.txt",'r').read().strip().split('\n') 
idmap_dict=dict() 
for line in idmap: 
    tokens=line.split('\t')
    hashname=tokens[0] 
    encodename=tokens[1] 
    idmap_dict[hashname]=encodename
#print(idmap_dict)
idr_file=open("idr.optimal.narrowPeak").read().strip().split('\n') 
overlap_file=open("overlap.optimal.narrowPeak",'r').read().strip().split('\n') 
outf_idr=open("idr.txt",'w') 
outf_overlap=open("overlap.txt",'w')
for line in idr_file: 
    tokens=line.split('/') 
    cur_hash=tokens[9] 
    try:
        cur_encodename=idmap_dict[cur_hash] 
        outf_idr.write(cur_encodename+'\t'+line+'\n')
    except: 
        print(cur_hash) 
for line in overlap_file: 
    tokens=line.split('/')
    cur_hash=tokens[9] 
    try:
        cur_encodename=idmap_dict[cur_hash] 
        outf_overlap.write(cur_encodename+'\t'+line+'\n') 
    except: 
        print(cur_hash) 
outf_idr.close() 
outf_overlap.close() 
