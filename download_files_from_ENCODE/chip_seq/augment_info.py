#!/usr/bin/env python
import argparse
import requests

file_name = "metadata_optimalidr_encodeprocessed_report.tsv"
augmented_file_name = (
    "augmented_metadata_optimalidr_encodeprocessed_report.tsv")

fh = open(file_name)
out_fh = open(augmented_file_name, 'w')
out_fh.write("file_id\tdataset\ttech_reps\tbio_reps\tdownload_url"
             +"\ttarget_label\tdescription\tbiosample\n")

for (i,line) in enumerate(fh):
    if (i > 1):
        line = line.rstrip()
        file_id, dataset, tech_reps, bio_reps, download_url = line.split("\t")
        dataset_url = "https://www.encodeproject.org"+dataset
        params = {'format': 'json'}
        print(dataset_url)
        r = requests.get(url = dataset_url, params = params)
        json = r.json()
        target_label = json['target']['label'].encode('utf-8')
        description = json['description'].encode('utf-8')
        biosample = json['biosample_summary'].encode('utf-8') 
        print(target_label)
        print(biosample)
        print(description)
        out_fh.write(
               file_id+"\t"+dataset+"\t"+tech_reps+"\t"+bio_reps
               +"\t"+download_url+"\t"+target_label
               +"\t"+biosample+"\t"+description+"\n")
        out_fh.flush()
        
fh.close()
out_fh.close()
