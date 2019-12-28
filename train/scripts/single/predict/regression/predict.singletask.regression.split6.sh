#!/bin/bash
kerasAC_predict_tdb \
    --batch_size 250 \
    --ref_fasta s3://encode-refs/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta \
    --tdb_indexer s3://encode-dnase-models/$1.task.tsv \
    --tdb_inputs seq \
    --tdb_input_source_attribute seq \
    --tdb_input_aggregation None \
    --tdb_input_transformation None \
    --tdb_input_flank 500 \
    --tdb_outputs s3://encode-dnase-models/$1.task.tsv \
    --tdb_output_source_attribute fc_bigwig \
    --tdb_output_flank 100 \
    --tdb_output_aggregation average \
    --tdb_output_transformation asinh \
    --num_inputs 1 \
    --num_outputs 1 \
    --tiledb_stride 50 \
    --genome hg38 --fold 6 \
    --chrom_sizes s3://encode-refs/hg38.chrom.sizes \
    --upsample_ratio_list_predict 1 \
    --predictions_and_labels_hdf5 s3://encode-models/predictions.ENCODE.dnase.regression.0 \
    --load_model_hdf5 s3://encode-dnase-models/ENCODE.dnase.regression.0.hdf5


		    
