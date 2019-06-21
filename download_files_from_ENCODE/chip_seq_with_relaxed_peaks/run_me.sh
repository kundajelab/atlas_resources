#!/usr/bin/env bash

curl -L "https://www.encodeproject.org/report.tsv?type=File&lab.title=ENCODE+Processing+Pipeline&status=released&field=%40id&field=accession&field=dataset&field=assembly&field=output_type&field=technical_replicates&field=biological_replicates&field=href&output_type%21=peaks&output_type%21=conservative+idr+thresholded+peaks&output_type%21=replicated+peaks&file_format=bed&output_type%21=sequence+alignability&output_type%21=methylation+state+at+CpG&output_type%21=methylation+state+at+CHH" > metadata_optimalandrelaxedpeaks_encodeprocessed.tsv
