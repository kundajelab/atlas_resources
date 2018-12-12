import argparse
import pandas as pd
from numpy import percentile,arcsinh
import pdb 
def parse_args():
    parser=argparse.ArgumentParser(description="assemble mean0 coverage columns from multiple columns, apply asinh, collapse to 1% and 90%")
    parser.add_argument("--input_files",nargs="+")
    parser.add_argument("--bed_file")
    parser.add_argument("--outf")
    parser.add_argument("--pad_bed_regions",type=int,default=0)
    return parser.parse_args()
def get_bed_dict(bed_file_name,pad_bed_regions):
    data=pd.read_csv(bed_file_name,header=None,sep='\t')
    data[1]=data[1]-pad_bed_regions
    data[2]=data[2]+pad_bed_regions
    bed_dict=dict() 
    for index,row in data.iterrows():
        chrom=row[0]
        startval=row[1]
        endval=row[2]
        label=row[3]
        bed_dict[label]=[chrom,str(startval),str(endval)]
    return bed_dict

def transform_coverage_values(input_file):
    data=pd.read_csv(input_file,header=None,sep='\t')
    labels=data[0]
    mean_vals=data[4]
    #transform with asinh
    mean_vals_asinh=arcsinh(mean_vals)
    #get bottom 1 % & top 90% and cap at those
    thresh_1_percent=percentile(mean_vals_asinh,1)
    thresh_90_percent=percentile(mean_vals_asinh,90)
    mean_vals_asinh[mean_vals_asinh < thresh_1_percent]=thresh_1_percent
    mean_vals_asinh[mean_vals_asinh > thresh_90_percent]=thresh_90_percent
    #run the min/max normalization
    normed=(mean_vals_asinh - thresh_1_percent)/(thresh_90_percent - thresh_1_percent)
    coverage_dict=dict()
    for i in range(len(labels)):
        coverage_dict[labels[i]]=normed[i]
    return coverage_dict
    
def main():
    args=parse_args()
    task_dict=dict()
    bed_dict=get_bed_dict(args.bed_file,args.pad_bed_regions)        
    print("parsed bed file to get label-> chrom,start,end map")
    for f in args.input_files: 
        task_dict[f]=transform_coverage_values(f)
        print("parsed:"+f)

    #aggregate into output file
    outf=open(args.outf,'w')
    tasks=list(task_dict.keys())
    outf.write("Chrom\tStart\tEnd\t"+'\t'.join(tasks)+'\n')
    regions=list(bed_dict.keys())
    regions.sort()
    for region_index in regions:
        outf.write('\t'.join(bed_dict[region_index]))
        coverage_vals=[task_dict[task][region_index] for task in tasks]
        outf.write('\t'+'\t'.join([str(i) for i in coverage_vals])+'\n')
        
if __name__=="__main__":
    main() 
