import pandas as pd 
import os 
experiments=pd.read_csv("ATAC_experiments.tsv",skiprows=1,sep='\t') 
files=pd.read_csv("ATAC_files.tsv",skiprows=1,sep='\t')
merged=files.merge(experiments,left_on='Dataset',right_on='ID')
filtered_merged=merged[merged['Output type']=='alignments'] 
downloads_file=open('download_atac_filtered_bams.txt','w') 
out_dir='/oak/stanford/groups/akundaje/projects/atlas/atac/input'
#pull down 
for index,row in filtered_merged.iterrows(): 
    experiment=row['Accession_y'] 
    experiment_folder='/'.join([out_dir,experiment])
    if os.path.exists(experiment_folder)==False: 
        os.makedirs(experiment_folder) 
    curl_url="https://www.encodeproject.org"+row['Download URL']
    print(curl_url) 
    #append the contents of the fastq.gz file to existing output file
    command=' '.join(['wget',curl_url,'-O','-','>',experiment_folder+'/'+row['Title']+'.bam'])
    downloads_file.write(command+'\n') 
downloads_file.close()
