#!/bin/bash
db_ingest --tiledb_metadata combined.encode.dnase.tasks.remaining.tsv \
	  --tiledb_group encode_dnase \
	  --overwrite \
	  --chrom_sizes hg38.chrom.sizes \
	  --chrom_threads 10 \
	  --attribute_config encode_pipeline \
	  --tile_size 10000 \
	  --batch_size 10000000 \
	  --write_chunk 10000000


