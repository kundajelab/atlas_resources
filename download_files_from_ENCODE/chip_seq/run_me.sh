#!/usr/bin/env bash
#Download a metadata tsv containing all ENCODE files where
#output_type="optimal idr thresholded peaks" and
#lab.title="ENCODE Processing Pipeline" and
#status=released and
#assembly=GRCh38 and
#format=bed

curl -L "https://www.encodeproject.org/report.tsv?type=File&output_type=optimal+idr+thresholded+peaks&lab.title=ENCODE+Processing+Pipeline&status=released&assembly=GRCh38&file_format=bed&field=%40id&field=dataset&field=technical_replicates&field=biological_replicates&field=href&limit=all" > metadata_optimalidr_encodeprocessed_report.tsv
./augment_info.py

cat metadata_optimalidr_encodeprocessed_report.tsv | perl -lane 'BEGIN {use File::Basename} if ($. > 2) {print "wget https://www.encodeproject.org/".$F[4]." -O ".basename($F[4])}' > download_script.sh

mkdir data
cd data
ln -s ../download_script.sh .
bash download_script.sh

#Get the line counts for the files, in order
for path in `perl -lane 'if ($. > 2) {print($F[4])}' augmented_metadata_optimalidr_encodeprocessed_report.tsv`; do file=`basename $path`; lines=`zcat "data/"$file | wc -l`; echo $lines; done > file_line_counts
paste augmented_metadata_optimalidr_encodeprocessed_report.tsv <(cat file_line_counts | perl -lane 'if ($. == 1) {print("linecount")} print $F[1]' | head) > with_line_counts_augmented_metadata_optimalidr_encodeprocessed_report.tsv

#remove temp files
rm file_line_counts
rm augmented_metadata_optimalidr_encodeprocessed_report.tsv
rm metadata_optimalidr_encodeprocessed_report.tsv
