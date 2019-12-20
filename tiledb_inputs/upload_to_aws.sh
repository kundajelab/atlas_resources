base_dir=/oak/stanford/groups/akundaje/projects/atlas/tiledb/encode_dnase
for cur_dir in `ls -d $base_dir/$1*`
do
aws s3 cp --recursive --quiet $cur_dir s3://encode-dnase/$cur_dir
echo $cur_dir
done
#
