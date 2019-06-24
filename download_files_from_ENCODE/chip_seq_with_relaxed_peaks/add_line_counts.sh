#!/usr/bin/env bash

#Get the line counts for the files, in order
for path in `perl -F"\t" -lane 'if ($. > 1) {print($F[7])}' metadata_optimalandrelaxedpeaks_encodeprocessed.tsv`; do file=`basename $path`; lines=`zcat "data/files_unorganized/"$file | wc -l`; echo $file" "$lines; done > file_line_counts
paste metadata_optimalandrelaxedpeaks_encodeprocessed.tsv <(cat file_line_counts | perl -lane 'if ($. == 1) {print("linecount")} print $F[1]') > withlinecounts_metadata_optimalandrelaxedpeaks_encodeprocessed.tsv
rm file_line_counts
