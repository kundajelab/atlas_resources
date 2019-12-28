#!/bin/bash
kerasAC_train \
    --batch_size 250 \
    --ref_fasta s3://encode-refs/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta \
    --tdb_indexer s3://encode-dnase-models/$1.task.tsv \
    --tdb_partition_attribute_for_upsample idr_peak \
    --tdb_partition_thresh_for_upsample 1 \
    --tdb_inputs seq \
    --tdb_input_source_attribute seq \
    --tdb_input_aggregation None \
    --tdb_input_transformation None \
    --tdb_input_flank 500 \
    --tdb_outputs s3://encode-dnase-models/$1.task.tsv \
    --tdb_output_source_attribute idr_peak \
    --tdb_output_flank 100 \
    --tdb_output_aggregation max \
    --tdb_output_transformation None \
    --num_inputs 1 \
    --num_outputs 1 \
    --genome hg38 \
    --fold 1 \
    --chrom_sizes s3://encode-refs/hg38.chrom.sizes \
    --upsample_ratio_list_train 0.7 \
    --upsample_ratio_list_eval 0.98 \
    --upsample_thresh_list_train 0 0.9 \
    --upsample_thresh_list_eval 0 0.9 \
    --num_train 100000 \
    --num_valid 10000 \
    --num_tasks 1 \
    --threads 0 \
    --max_queue_size 100 \
    --patience 3 \
    --patience_lr 2 \
    --model_prefix s3://encode-dnase-models/$1.regression.0 \
    --architecture_spec functional_basset_regression_1D \
    --use_multiprocessing False \
    --num_gpus 1 \
    --weights s3://encode-dnase-models/ENCODE.dnase.classification.0.weights



