#!/bin/bash
python generate_pipeline_inputs.py --fastq_dir /oak/stanford/groups/akundaje/projects/atlas/dnase_fastqs \
       --pipeline_json_dir /oak/stanford/groups/akundaje/projects/atlas/hg38_dnase_jsons \
       --pipeline_output_dir /oak/stanford/groups/akundaje/projects/atlas/dnase_processed \
       --caper_submit_script /oak/stanford/groups/akundaje/projects/atlas/caper_submit_hg38_dnase.sh
