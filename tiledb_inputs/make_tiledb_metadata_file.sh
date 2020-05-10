#--id_to_task /oak/stanford/groups/akundaje/projects/atlas/dnase_processed/processed_encode_ids.txt \
basedir=/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs
python make_tiledb_metadata_file.py --fc_bigwig $basedir/fc_bigwig \
    --pval_bigwig $basedir/pval_bigwig \
    --count_bigwig_plus_5p $basedir/bpnet.5pcounts.plus.txt \
    --count_bigwig_minus_5p $basedir/bpnet.5pcounts.minus.txt \
    --count_bigwig_unstranded_5p $basedir/bpnet.5pcounts.unstranded.txt \
    --idr_peak $basedir/idr.optimal.narrowPeak \
    --overlap_peak $basedir/overlap.optimal.narrowPeak \
    --ambig_peak $basedir/ambiguous.optimal.narrowPeak \
    --id_to_task /oak/stanford/groups/akundaje/projects/atlas/dnase_processed/processed_all.txt \
    --outf encode.dnase.tasks \
    --split_tasks_to_separate_files
