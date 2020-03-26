#!/bin/bash
find "/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/atac"  -wholename "*/call-bam2ta/shard-0/execution/*.merged.nodup.tagAlign.gz" | grep -v "glob" > merged.nodup.tagAligns.txt


