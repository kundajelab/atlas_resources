#python aggregate_ataqc.py --ataqc_files /oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/qc.json.txt \
#       --outf atlas_metadata_summary.txt \
#       --mitra_prefix http://mitra.stanford.edu/kundaje/projects/atlas \
#       --prefix_to_drop_for_oak /oak/stanford/groups/akundaje/projects/atlas \
#       --hash_to_id /oak/stanford/groups/akundaje/projects/atlas/dnase_processed/processed_all.txt \
#       --fname_hash_index 9

python aggregate_ataqc.py --ataqc_files qc.json.1.txt \
       --outf atlas_metadata_summary.1.txt \
       --mitra_prefix http://mitra.stanford.edu/kundaje/projects/atlas \
       --prefix_to_drop_for_oak /oak/stanford/groups/akundaje/projects/atlas \
       --hash_to_id /oak/stanford/groups/akundaje/projects/atlas/dnase_processed/processed_all.txt \
       --fname_hash_index 9

#python aggregate_ataqc.py --ataqc_files qc.json.2.txt \
#       --outf atlas_metadata_summary.2.txt \
#       --mitra_prefix http://mitra.stanford.edu/kundaje/projects/atlas \
#       --prefix_to_drop_for_oak /oak/stanford/groups/akundaje/projects/atlas \
#       --hash_to_id /oak/stanford/groups/akundaje/projects/atlas/dnase_processed/processed_all.txt \
#       --fname_hash_index 9

