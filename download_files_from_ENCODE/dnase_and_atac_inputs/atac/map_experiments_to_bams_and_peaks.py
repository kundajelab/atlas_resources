import argparse
import pandas as pd

def parse_args():
    parser=argparse.ArgumentParser(description="map ENCODE experiment filtered bams --> overlap peaks --> idr peaks")
    parser.add_argument("--experiment_file",default="/oak/stanford/groups/akundaje/projects/atlas/atac/input/ATAC_experiments.tsv")
    parser.add_argument("--filtered_bams_file",default="/oak/stanford/groups/akundaje/projects/atlas/atac/input/all.filtered_bams.txt")
    parser.add_argument("--overlap_peaks_file",default="/oak/stanford/groups/akundaje/projects/atlas/atac/input/overlap_files.txt")
    parser.add_argument("--idr_peaks_file",default="/oak/stanford/groups/akundaje/projects/atlas/atac/input/idr_files.txt")
    parser.add_argument("--outf",default="/oak/stanford/groups/akundaje/projects/atlas/atac/input/experiment_to_file_types.txt")
    return parser.parse_args()


def main():
    args=parse_args()
    filtered_bam_dict={}
    overlap_peak_dict={}
    idr_peak_dict={}
    
    #parse individual file types
    filtered_bam_files=open(args.filtered_bams_file,'r').read().strip().split('\n')
    for filtered_bam_file in filtered_bam_files:
        filtered_bam_dict[filtered_bam_file.split('/')[-1].split('.')[0]]=1

    overlap_peak_files=open(args.overlap_peaks_file,'r').read().strip().split('\n')
    for overlap_peak_file in overlap_peak_files[1::]:
        overlap_peak_dict[overlap_peak_file.split('/')[-1].split('.')[0]]=1         

    idr_peak_files=open(args.idr_peaks_file,'r').read().strip().split('\n')
    for idr_peak_file in idr_peak_files[1::]:
        idr_peak_dict[idr_peak_file.split('/')[-1].split('.')[0]]=1

    experiments=pd.read_csv(args.experiment_file,header=0,skiprows=1,sep='\t')
    outf=open(args.outf,'w')
    outf.write('Experiment\tFilteredBams\tOverlapPeaks\tIDRPeaks\n')
    for index,row in experiments.iterrows():
        experiment=row['Accession']
        files=row['Files'].replace('/','').replace('files','').split(',')
        cur_bams=[]
        cur_overlaps=[]
        cur_idr=[]
        for filename in files:
            if filename in filtered_bam_dict:
                cur_bams.append(filename)
            if filename in overlap_peak_dict:
                cur_overlaps.append(filename)
            if filename in idr_peak_dict:
                cur_idr.append(filename)
        outf.write(experiment+'\t'+','.join(cur_bams)+'\t'+','.join(cur_overlaps)+'\t'+','.join(cur_idr)+'\n')
    outf.close()
    
    

if __name__=="__main__":
    main()
    
    
