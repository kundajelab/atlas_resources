#!/usr/bin/env bash

cat metadata_optimalandrelaxedpeaks_encodeprocessed.tsv | perl -F"\t" -ane 'BEGIN {use File::Basename} if ($. > 1) {$last = $F[7]; $last =~ s/\n//g; $last =~ s/\r//g; print "wget https://www.encodeproject.org/".$last." -O ".basename($last)."\n"}' > download_script.sh

mkdir data
cd data
mkdir files_unorganized
cd files_unorganized
mv ../../download_script.sh .
bash download_script.sh
