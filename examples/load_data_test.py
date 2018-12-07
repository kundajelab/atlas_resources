"""description: testing the data loader
"""

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

    use_queues = True
    
    # set up dataloader
    data_loader = H5DataLoader(
        data_dir=data_dir,
        fasta=fasta)
    
    # build an input fn
    input_fn = data_loader.build_input_fn(
        32,
        targets=[([("LABELS", [])],{})],
        use_queues=use_queues)
    
    # set up graph to run
    with tf.Graph().as_default() as g:

        if use_queues:
            features, _ = input_fn()
        else:
            iterator = input_fn().make_one_shot_iterator()
            features, _ = iterator.get_next()


        # start a sess
        sess, coord, threads = setup_tensorflow_session()

        sess.run(features[DataKeys.FEATURES])

        quit()
        
        results = sess.run([
            features[DataKeys.FEATURES],
            features[DataKeys.LABELS]])
        
        print results
        
        # close it out
        close_tensorflow_session(coord, threads)
    
    return


load_data_test()
