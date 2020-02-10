#!/bin/bash 
for i in 0 1
do 
    sbatch -J $i -o logs/$i.o -e logs/$i.e -p akundaje,euan,normal,owners --mem=120G x$i.sh
done
