idr_peaks=open('idr.txt','r').read().strip().split('\n') 
overlap_peaks=open('overlap.txt','r').read().strip().split('\n') 
tagaligns=open('tagAligns.txt','r').read().strip().split('\n') 
idr_dict=dict() 
overlap_dict=dict() 
tagalign_dict=dict() 

for line in idr_peaks: 
    tokens=line.split('\t') 
    encode_id=tokens[0] 
    if encode_id not in  idr_dict: 
        idr_dict[encode_id]=tokens[1] 
for line in overlap_peaks: 
    tokens=line.split('\t') 
    encode_id=tokens[0] 
    if encode_id not in overlap_dict: 
        overlap_dict[encode_id]=tokens[1] 
for line in tagaligns: 
    tokens=line.split('\t') 
    encode_id=tokens[0] 
    if encode_id not in tagalign_dict:
        tagalign_dict[encode_id]=tokens[1] 
        
outf_idr=open('idr.filtered.txt','w') 
for key in idr_dict: 
    outf_idr.write(key+'\t'+idr_dict[key]+'\n')
outf_idr.close() 

outf_overlap=open('overlap.filtered.txt','w') 
for key in overlap_dict: 
    outf_overlap.write(key+'\t'+overlap_dict[key]+'\n') 
outf_overlap.close() 

outf_tagalign=open('tagAlign.filtered.txt','w') 
for key in tagalign_dict: 
    outf_tagalign.write(key+'\t'+tagalign_dict[key]+'\n') 
outf_tagalign.close()
