#!/usr/bin/env bash

#Download a metadata tsv containing all ENCODE files where
#status=released and
#assembly=GRCh38 and
#assay_title=DNAse-seq
#format=fastq
#experiment info 
curl -L "https://www.encodeproject.org/report.tsv?type=Experiment&status=released&assay_title=DNase-seq&assembly=GRCh38" > experiments.tsv
#file info
curl -L "https://www.encodeproject.org/report.tsv?type=File&file_format=fastq"> files.tsv 
