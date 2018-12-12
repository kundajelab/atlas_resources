#DNase
bedfile=gecco_v2.train.200center.bed
split=train

for file in C31 C34 C36 V389 V410 V576
do
    bigWigAverageOverBed dnase/fastq/$file/$file\_out/signal/macs2/rep1/$file\_DNase.trim.nodup.pf.fc.signal.bigwig $bedfile $file\_DNase.$split.bed &
done
for file in V429 V9P V855 V5 V457 V703 V968 V456 V432 V940 V410 C37 V1051 V1009 V206 V481 V784 V852 V1024 V576 V866 C29 C28 V411
do
    bigWigAverageOverBed h3k27ac/$file\_H3K27ac/$file\_out/signal/macs2/rep1/$file\_H3K27ac.nodup.tagAlign_x_$file\_Input.nodup.tagAlign.fc.signal.bw $bedfile $file\_H3K27ac.$split.bed &
done


