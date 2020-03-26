#!/bin/bash
find "/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/atac"  -wholename "*/call-qc_report/execution/qc.html" > qc.html.txt
find "/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/atac"  -wholename "*/call-qc_report/execution/qc.json" > qc.json.txt

