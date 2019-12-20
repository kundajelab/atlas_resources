#!/bin/bash
#for task in `cat tasks` 
for task in `cat tasks.remaining` 
do 
    sbatch -J $task -o logs/$task.o -e logs/$task.e -p euan,akundaje,owners --mem=80G -t 1-0 run_db_ingest_single_threaded.sh $task 
done
