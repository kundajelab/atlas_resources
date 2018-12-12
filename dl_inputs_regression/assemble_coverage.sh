python assemble_coverage.py --input_files coverage/*train.bed \
       --bed_file gecco_v2.train.200center.bed \
       --outf coverage.train.bed &


python assemble_coverage.py --input_files coverage/*validate.bed \
       --bed_file gecco_v2.validate.200center.bed \
       --outf coverage.validate.bed &

python assemble_coverage.py --input_files coverage/*test.bed \
       --bed_file gecco_v2.test.200center.bed \
       --outf coverage.test.bed &

