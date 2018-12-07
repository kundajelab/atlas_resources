DATA_DIR=/users/dskim89/git/dragonn_benchmark_data/GECCO
WORK_DIR=/srv/scratch/dskim89/atlas/test.2018-12-06.datalayer
ANNOTATIONS=/mnt/lab_data/kundaje/users/dskim89/annotations/tronn_preprocess_annotations.json

LABELS=$DATA_DIR/easy.V576.dinuc.1neg.1pos.train.bed.gz

tronn preprocess --annotations $ANNOTATIONS \
      --labels LABELS=$LABELS \
      -o $WORK_DIR/test_dataset \
      --prefix gecco
