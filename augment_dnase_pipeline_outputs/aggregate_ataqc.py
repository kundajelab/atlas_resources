import argparse
import collections 
import json 
import pdb 

def parse_args(): 
    parser=argparse.ArgumentParser(description="aggregate ataqc metrics for all samples in a single report")
    parser.add_argument("--ataqc_files",default="/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/qc.json.txt") 
    parser.add_argument("--outf",default="atlas.metadata.report.txt") 
    parser.add_argument("--mitra_prefix",default="http://mitra.stanford.edu/kundaje/projects/atlas/") 
    parser.add_argument("--prefix_to_drop_for_oak",default="/oak/stanford/groups/akundaje/projects/atlas/")
    parser.add_argument("--hash_to_id",default="/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/processed_all.txt")
    parser.add_argument("--fname_hash_index",type=int,default=9)
    return parser.parse_args() 


def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def iterate_json(data,val_dict,all_keys,cur_id):
    flat_data=flatten(data)
    for key in flat_data:
        if key not in all_keys:
            all_keys.add(key)
        val_dict[cur_id][key]=flat_data[key]
    return val_dict,all_keys

def main(): 
    args=parse_args() 
    ataqc_files=open(args.ataqc_files,'r').read().strip().split('\n')
    val_dict=dict()
    all_keys=set([]) 
    outf=open(args.outf,'w')
    hash_to_id=open(args.hash_to_id,'r').read().strip().split('\n')
    hash_to_id_dict=dict()
    for line in hash_to_id:
        tokens=line.split('\t')
        cur_hash=tokens[0]
        cur_id=tokens[1]
        hash_to_id_dict[cur_hash]=cur_id
    for fname in ataqc_files:
        with open(fname,'r') as cur_f:
            data=json.load(cur_f)
        #get the report title
        report_title=fname.replace(args.prefix_to_drop_for_oak,args.mitra_prefix).replace(".json",".html")
        #get the hash
        cur_hash=fname.split('/')[args.fname_hash_index]
        cur_id=hash_to_id_dict[cur_hash]
        print(cur_id+" : "+report_title)
        val_dict[cur_id]=dict()
        val_dict[cur_id]['path']=report_title
        all_keys.add('path')        
        #iterate through the json file recursively
        val_dict,all_keys=iterate_json(data,val_dict,all_keys,cur_id)
        
    outf.write('Dataset')
    all_keys=list(all_keys) 
    for key in all_keys:
        outf.write('\t'+key)
    outf.write('\n')
    for dataset in val_dict:
        outf.write(dataset)
        for key in all_keys:
            if key in val_dict[dataset]:
                outf.write('\t'+str(val_dict[dataset][key]))
            else:
                outf.write('\tNA')
        outf.write('\n')
    outf.close()

if __name__=="__main__": 
    main() 
