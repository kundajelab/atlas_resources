#!/bin/bash 
#single or multi
single_multi=$1
echo $single_multi
train_predict=$2
echo $train_predict
classification_regression=$3
echo $classification_regression
fold=$4
echo $fold
task=$5
echo $task
if [ "$single_multi" == "single" ];
then
    bash single/$train_predict/$classification_regression/$train_predict.singletask.$classification_regression.split$fold.sh $task
fi

if [ "$single_multi" == "multi" ];
then
    bash multi/$train_predict/$classification_regression/$train_predict.multitask.$classification_regression.split$fold.sh
fi
   
   

