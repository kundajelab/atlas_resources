#!/usr/bin/env bash
#Download a metadata tsv containing all ENCODE files where
#output_type="optimal idr thresholded peaks" and
#lab.title="ENCODE Processing Pipeline" and
#status=released and
#assembly=GRCh38 and
#format=bed

curl https://www.encodeproject.org/report.tsv?type=File&output_type=optimal+idr+thresholded+peaks&lab.title=ENCODE+Processing+Pipeline&status=released&assembly=GRCh38&file_format=bed&field=%40id&field=dataset&field=technical_replicates&field=biological_replicates&field=href&limit=all > metadata_optimalidr_encodeprocessed_report.tsv
