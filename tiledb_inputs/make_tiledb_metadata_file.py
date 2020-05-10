import argparse
import pdb 
import pandas as pd
#order of tasks is fixed 
fields=['fc_bigwig','pval_bigwig','idr_peak','overlap_peak','ambig_peak','count_bigwig_plus_5p','count_bigwig_minus_5p','count_bigwig_unstranded_5p']
def parse_args():
    parser=argparse.ArgumentParser(description="form tiledb metadata")
    parser.add_argument("--fc_bigwig",default=None)
    parser.add_argument("--pval_bigwig",default=None)
    parser.add_argument("--idr_peak",default=None)
    parser.add_argument("--overlap_peak",default=None)
    parser.add_argument("--ambig_peak",default=None)
    parser.add_argument("--count_bigwig_plus_5p",default=None)
    parser.add_argument("--count_bigwig_minus_5p",default=None)
    parser.add_argument("--count_bigwig_unstranded_5p",default=None)
    parser.add_argument("--id_to_task",help="2-column file, the first column contains the pipeline id, the 2nd column containsn the ENCODE identifier (task name)")
    parser.add_argument("--outf")
    parser.add_argument("--split_tasks_to_separate_files",action="store_true",default=False)
    return parser.parse_args()

def write_output_file_per_task(args,task_dict,task):
    #print(task)
    outf=open(args.outf+"."+str(task),'w')
    outf.write('dataset'+'\t'+'\t'.join(fields)+'\n')
    outf.write(task) 
    for field in fields:
        try:
            outf.write('\t'+task_dict[task][field])
        except:
            print("not found:"+field+'\t'+task_dict[task]['cromwell_id']+'\t'+task)
            outf.write('\tNA')
    outf.write('\n')
    
def write_output_file_all_tasks(args,task_dict):
    outf=open(args.outf,'w')
    outf.write('dataset'+'\t'+'\t'.join(fields)+'\n')
    for task in task_dict:
        outf.write(task)
        for field in fields: 
            try:
                outf.write('\t'+task_dict[task][field])
            except:
                print("not found:"+field+'\t'+task_dict[task]['cromwell_id']+'\t'+task)
                outf.write('\tNA')
def get_field_dict(text_field,args_field,task_dict,id_to_task):
    if args_field is None:
        for task in task_dict: 
            task_dict[task][text_field]=None
    else:
        for line in open(args_field,'r').read().strip().split('\n'):
            tokens=line.split('/')
            for token in tokens:
                if token in id_to_task:
                    cur_task=id_to_task[token]
                    if cur_task not in task_dict:
                        task_dict[cur_task]=dict()
                        task_dict[cur_task]['cromwell_id']=token 
                    task_dict[cur_task][text_field]=line
                    break
    return task_dict 

def main():
    args=parse_args()
    #create a dictionary of cromwell hash values to encode id's 
    id_to_task=pd.read_csv(args.id_to_task,header=None,sep='\t',index_col=0).to_dict()[1]
    
    #create a dictionary to keep track of task files
    task_dict=dict()
    #iterate through each of the fields
    task_dict=get_field_dict('fc_bigwig',args.fc_bigwig,task_dict,id_to_task)
    #print(task_dict)
    #print("parsed fc_bigwig") 
    task_dict=get_field_dict('pval_bigwig',args.pval_bigwig,task_dict,id_to_task)
    #print("parsed pval_bigwig")
    task_dict=get_field_dict('count_bigwig_plus_5p',args.count_bigwig_plus_5p,task_dict,id_to_task)
    #print("parsed count_bigwig_plus_5p") 
    task_dict=get_field_dict('count_bigwig_minus_5p',args.count_bigwig_minus_5p,task_dict,id_to_task)
    #print("parsed count_bigwig_minus_5p")
    task_dict=get_field_dict('count_bigwig_unstranded_5p',args.count_bigwig_unstranded_5p,task_dict,id_to_task)
    #print("parsed count_bigwig_unstranded_5p")
    task_dict=get_field_dict('idr_peak',args.idr_peak,task_dict,id_to_task)
    #print("parsed idr_peak") 
    task_dict=get_field_dict('overlap_peak',args.overlap_peak,task_dict,id_to_task)
    #print("parsed overlap_peak") 
    task_dict=get_field_dict('ambig_peak',args.ambig_peak,task_dict,id_to_task)
    #print("parsed ambig_peak")
    #print(task_dict)
    #generate output file(s)
    #pdb.set_trace() 
    if args.split_tasks_to_separate_files is True:
        for task in task_dict:
            write_output_file_per_task(args,task_dict,task)
    else:
        write_output_file_all_tasks(args,task_dict)
    
    
    

if __name__=="__main__":
    main()
    
    
    
