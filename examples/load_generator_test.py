"""description: testing the data loader
"""

import threading

import tensorflow as tf

from tronn.datalayer import H5DataLoader
from tronn.util.tf_utils import setup_tensorflow_session
from tronn.util.tf_utils import close_tensorflow_session

from tronn.util.utils import DataKeys

def load_data_test():
    """load data
    """
    data_dir = "/srv/scratch/dskim89/atlas/test.2018-12-06.datalayer/test_dataset/h5"
    fasta = "/mnt/data/annotations/by_release/hg19.GRCh37/hg19.genome.fa"
    
    # set up dataloader
    data_loader = H5DataLoader(
        data_dir=data_dir,
        fasta=fasta)

    # build a generator for one of the files
    generator, dtypes_dict, shapes_dict = data_loader.build_generator(
        batch_size=32,
        targets=[([("LABELS", [])],{})],
        shuffle=True,
        lock=threading.Lock())

    h5_to_generator = generator(data_loader.data_files[0], yield_single_examples=False)

    # get batches as numpy arrays
    results = h5_to_generator.next()[0]
    
    # print shapes to show features
    print "metadata:", results[DataKeys.SEQ_METADATA].shape
    print "features:", results[DataKeys.FEATURES].shape
    print "^ note not yet onehot encoded (on-the-fly in my other code)"
    print "labels:", results[DataKeys.LABELS].shape

    # one example of metadata read out
    print "metadata for one example:", str(results[DataKeys.SEQ_METADATA][0][0])
    
    return


load_data_test()
