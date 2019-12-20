#!/bin/bash 
db_ingest_single_threaded --tiledb_metadata task_specific/encode.dnase.tasks.$1 \
    --tiledb_group encode_dnase \
    --overwrite \
    --chrom_sizes /oak/stanford/groups/akundaje/projects/atlas/hg38.chrom.sizes \
    --tile_size 10000 \
    --write_chunk 10000000
