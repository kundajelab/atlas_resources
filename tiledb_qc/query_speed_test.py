#import dependencies
import pandas as pd 
import numpy as np
import tiledb 
import random 
import timeit

#set random seed
random.seed(1234)

def make_regions(chrom,chromsize,batch_size,vector_length):
    '''
    generates random genomewide coordinate batch for querying tiledb 
    '''
    regions=[]
    for batch_entry in range(batch_size): 
        cur_chrom_start=random.randint(0,chromsize-vector_length)
        regions.append([chrom,cur_chrom_start,cur_chrom_start+vector_length])
    return regions 

def open_tdb_remote(task,chrom,ctx):
    '''
    opens remote tiledb database containing data for a user-specified task/chromosome
    '''
    return tiledb.DenseArray("s3://encode-dnase/"+task+"."+chrom,mode='r',ctx=ctx)

def open_tdb_local(task,chrom,ctx):
    '''
    opens local tiledb database containing data for a user-specified task/chromosome
    '''
    return tiledb.DenseArray('.'.join([task,chrom]),mode='r',ctx=ctx)


def query_tdb(tdb_instance,regions,batch_size,vector_length,attribute_of_interest):
    '''
    queries a batch of data from DenseArray
    '''
    #create a placeholder numpy array to store batch data 
    batch=np.full((batch_size,vector_length),np.nan)
    for region_index in range(len(regions)):
        region=regions[region_index]
        cur_start=region[1]
        cur_end=region[2]
        batch[region_index,:]=tdb_instance[cur_start:cur_end][attribute_of_interest]
    return batch


def main():
    #attributes for data query
    attribute_of_interest='fc_bigwig'
    batch_size=100
    vector_length=1000
    task="ENCSR000EID"
    chrom='chr1'
    chromsize=248956422

    #create tiledb context 
    tdb_config=tiledb.Config()
    tdb_config['vfs.s3.region']='us-west-1'    
    ctx=tiledb.Ctx(config=tdb_config)
    print("created tdb context")
    
    #generate a batch of genomic regions 
    regions=make_regions(chrom,chromsize,batch_size,vector_length)
    print("generated batch of coordinates to use in queries")
    
    #open remote tiledb instance
    tdb_instance_remote=open_tdb_remote(task,chrom,ctx)
    print("opened remote tdb") 
    #query batch of data from open remote tdb 
    timeit.timeit(batch_from_tdb_remote=query_tdb(tdb_instance_remote,regions,batch_size,vector_length,attribute_of_interest),number=5)
    print("queried remote tdb")
    
    #open local tiledb instance
    tdb_instance_local=open_tdb_local(task,chrom,ctx)
    print("opened local tdb") 
    #query batch of data from open local tiledb
    timeit.timeit(batch_from_tdb_local=query_tdb(tdb_instance_local,regions,batch_size,vector_length,attribute_of_interest),number=5)
    print("queried local tdb") 

if __name__=="__main__":
    main()
    
