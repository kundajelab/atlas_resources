#!/usr/bin/env python
from __future__ import division, print_function
import argparse
import requests
import json as js

file_name = "metadata_optimalidr_encodeprocessed_report.tsv"
augmented_file_name = (
    "augmented_metadata_optimalidr_encodeprocessed_report.tsv")

fh = open(file_name)
out_fh = open(augmented_file_name, 'w')
out_fh.write("file_id\tdataset\ttech_reps\tbio_reps\tdownload_url"
             +"\ttarget_label\tbiosample_short_name\tmod_or_treament"
             +"\tlab"
             +"\tbiosample_summary\tdescription"
             +"\tbiosample_accession\tbiosample_ontology_id"
             +"\tbiosample_treatments"
             +"\tbiosample_applied_mods"
             +"\tbiosample_genetic_mods"
             +"\n")

for (i,line) in enumerate(fh):
    if (i > 1):
        line = line.rstrip()
        file_id, dataset, tech_reps, bio_reps, download_url = line.split("\t")
        dataset_url = "https://www.encodeproject.org"+dataset
        print(dataset_url)
        params = {'format': 'json'}
        r = requests.get(url = dataset_url, params = params)
        json = r.json()
        target_label = json['target']['label'].encode('utf-8')
        description = json['description'].encode('utf-8')
        lab = json['lab']['name'].encode('utf-8').replace(" ","-")
        biosample_ontology_id = json['biosample_ontology']['term_id'].encode('utf-8')
        biosample_ontology_term_name = json['biosample_ontology']['term_name'].encode('utf-8')
        biosample_ontology_term_name =\
            biosample_ontology_term_name.replace(" ","-")

        #biosample accessions for the different reps
        biosample_accessions = set([x['library']['biosample']['accession'].encode('utf-8') for
                                    x in json['replicates']])

        biosample_applied_mods = list(set(
            [len(x['library']['biosample']['applied_modifications'])
             for x in json['replicates']]))
        assert len(biosample_applied_mods)==1 #each replicate should have same mods
        biosample_applied_mods = biosample_applied_mods[0]

        biosample_genetic_mods = list(set(
            [len(x['library']['biosample']['genetic_modifications'])
             for x in json['replicates']]))
        assert len(biosample_genetic_mods)==1 #each replicate should have same mods
        biosample_genetic_mods = biosample_genetic_mods[0]

        biosample_treatments = list(set(
            [len(x['library']['biosample']['treatments'])
             for x in json['replicates']]))
        assert len(biosample_treatments)==1 #each replicate should have same treatments
        biosample_treatments = biosample_treatments[0]

        biosample_summary = json['biosample_summary'].encode('utf-8') 

        #flag for things that are modified or treated
        modortreat_detected = (
            "has-mod-or-treatment" if
            (biosample_genetic_mods
             +biosample_applied_mods+biosample_treatments > 0)
            else "no-mod-or-treatment")

        #some sanity checks
        if (biosample_summary != biosample_ontology_term_name):
            if (biosample_treatments
                +biosample_genetic_mods
                +biosample_applied_mods==0):
                print("No mod or treatment listed")
                print(biosample_ontology_term_name, modortreat_detected)
                print(biosample_summary)

        if (biosample_treatments
            +biosample_genetic_mods
            +biosample_applied_mods > 0):
            if (biosample_summary == biosample_ontology_term_name):
                print("Mods listed but not in biosample summary")
                print(biosample_ontology_term_name, modortreat_detected)
                print(biosample_summary)

        line_to_write = (
               file_id+"\t"+dataset+"\t"+tech_reps+"\t"+bio_reps
               +"\t"+download_url+"\t"+target_label
               +"\t"+biosample_ontology_term_name+"\t"+modortreat_detected
               +"\t"+lab
               +"\t"+biosample_summary+"\t"+description
               +"\t"+",".join(biosample_accessions)
               +"\t"+biosample_ontology_id
               +"\t"+str(biosample_treatments)
               +"\t"+str(biosample_applied_mods)
               +"\t"+str(biosample_genetic_mods)+"\n")
        out_fh.write(line_to_write)
        out_fh.flush()
        
fh.close()
out_fh.close()
