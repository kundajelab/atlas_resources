#!/usr/bin/env bash

#Download a metadata tsv containing all ENCODE files where
#output_type="optimal idr thresholded peaks" or
# "peaks and background for input to idr", specified
# as a complement: output_type%21=peaks&output_type%21=conservative+idr+thresholded+peaks&output_type%21=replicated+peaks&output_type%21=sequence+alignability&output_type%21=methylation+state+at+CpG&output_type%21=methylation+state+at+CHH
#lab.title="ENCODE Processing Pipeline" and
#status=released and
#assembly=GRCh38 and
#format=bed

#Query has been updated to have case sensitivity...used to be "idr", but now has to be IDR
# Good idea to manually inspect to make sure query is working as expected since apparently the API changes from time to time.
#Also rather than using complement-type syntax to specify the desired files, going forward it may be better to list out the desired file types, which is
# achieved by the following query: https://www.encodeproject.org/report/?type=File&lab.title=ENCODE+Processing+Pipeline&status=released&assembly=GRCh38&file_format=bed&output_type=peaks+and+background+as+input+for+IDR&output_type=optimal+IDR+thresholded+peaks&field=%40id&field=accession&field=dataset&field=assembly&field=output_type&field=technical_replicates&field=biological_replicates&field=href
curl -L "https://www.encodeproject.org/report.tsv?type=File&lab.title=ENCODE+Processing+Pipeline&status=released&assembly=GRCh38&field=%40id&field=accession&field=dataset&field=assembly&field=output_type&field=technical_replicates&field=biological_replicates&field=href&file_format=bed&output_type%21=peaks&output_type%21=conservative+IDR+thresholded+peaks&output_type%21=replicated+peaks&output_type%21=sequence+alignability&output_type%21=methylation+state+at+CpG&output_type%21=methylation+state+at+CHH&output_type%21=methylation+state+at+CHG&output_type%21=enrichment&output_type%21=hotspots&output_type%21=pseudoreplicated+IDR+thresholded+peaks&output_type%21=stable+peaks&output_type%21=transcription+start+sites" > unordered_metadata_optimalandrelaxedpeaks_encodeprocessed.temp

#Go through a sorting step to make the order deterministic (it's not deterministic when pulled from web)
#Also filter for files that don't use more than one biological replicate
#Also strip annoying carraige return characters

cat unordered_metadata_optimalandrelaxedpeaks_encodeprocessed.temp | head -2 | tail -1 | perl -lne '$_ =~ s/\r//g; print $_' > title.temp
cat unordered_metadata_optimalandrelaxedpeaks_encodeprocessed.temp | perl -lane 'if ($. > 2) {print $_}' | perl -F"\t" -lane 'if (length($F[6]) > 1) {$_ =~ s/\r//g; print $_}' | sort > sorted_rows.temp

cat title.temp sorted_rows.temp > metadata_optimalandrelaxedpeaks_encodeprocessed.tsv

rm unordered_metadata_optimalandrelaxedpeaks_encodeprocessed.temp
rm title.temp
rm sorted_rows.temp
