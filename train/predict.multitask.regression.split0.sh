#!/bin/bash
kerasAC_predict \
    --batch_size 20 \
    --ref_fasta /mnt/data/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta \
    --tdb_indexer s3://encode-dnase-models/encode.dnase.tasks.tsv \
    --tdb_inputs seq \
    --tdb_input_source_attribute seq \
    --tdb_input_aggregation None \
    --tdb_input_transformation None \
    --tdb_input_flank 500 \
    --tdb_outputs s3://encode-dnase-models/encode.dnase.tasks.tsv \
    --tdb_output_source_attribute fc_bigwig \
    --tdb_output_flank 100 \
    --tdb_output_aggregation mean \
    --tdb_output_transformation asinh \
    --num_inputs 1 \
    --num_outputs 1 \
    --tiledb_stride 50 \
    --predict_chroms chr1 \
    --chrom_sizes s3://encode-refs/hg38.chrom.sizes \
    --upsample_ratio_list_predict 1 \
    --predictions_and_labels_hdf5 s3://encode-models/predictions.ENCODE.dnase.regression.0 \
    --threads 20 \
    --max_queue_size 100 \
    --model_hdf5 s3://encode-models/ENCODE.dnase.regression.0


		    
