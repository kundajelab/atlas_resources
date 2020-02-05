#import dependencies
import pandas as pd 
import numpy as np
import tiledb 
import random 
import time

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
    t0=time.time() 
    tdb_instance_remote=open_tdb_remote(task,chrom,ctx)
    t1=time.time()
    delta1=(t1-t0)*1000
    print("opened remote tdb: "+str(delta1)+ "ms")
    
    #query batch of data from open remote tdb
    t2=time.time() 
    batch_remote=query_tdb(tdb_instance_remote,regions,batch_size,vector_length,attribute_of_interest)
    t3=time.time()
    delta2=(t3-t2)*1000 #milliseconds 
    print("queried remote tdb: "+str(delta2) +" ms")
    
    #open local tiledb instance
    t4=time.time() 
    tdb_instance_local=open_tdb_local(task,chrom,ctx)
    t5=time.time()
    delta3=(t5-t4)*1000
    print("opened local tdb: "+str(delta3)+" ms")
    
    #query batch of data from open local tiledb
    t6=time.time()
    batch_local=query_tdb(tdb_instance_local,regions,batch_size,vector_length,attribute_of_interest)
    t7=time.time()
    delta4=(t7-t6)*1000
    print("queried local tdb: "+str(delta4)+" ms") 

if __name__=="__main__":
    main()
    
