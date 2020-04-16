input_bam=$1
#name sort to achieve random genomic pos
samtools sort -n --threads 50 -O bam -o $input_bam.namesorted.bam $input_bam
#echo "done sorting" 
samtools view -H $input_bam.namesorted.bam > $input_bam.pr1.sam
cp $input_bam.pr1.sam $input_bam.pr2.sam
#echo "made headers"
sam1=$input_bam.pr1.sam
sam2=$input_bam.pr2.sam 
samtools view --threads 50  $input_bam.namesorted.bam | awk -v sam1="$sam1" -v sam2="$sam2" '{if(NR%2){print >> sam1} else {print >> sam2}}'
