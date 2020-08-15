
# ENCODE DNASE 

The outputs are found here: 

`/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/aggregate_outputs/`

The map of pipeline hash to ENCODE ID is here: 

`/oak/stanford/groups/akundaje/projects/atlas/dnase_processed/processed_all.txt`

## pipeline outputs
* bowtie2_bams.txt -- unfiltered bam files 
* fc_bigwig -- fold change bigwigs
* pval_bigwig -- pval bigwigs 
* merged.nodup.tagAligns.txt -- filtered tagAligns 
* overlap.optimal.narrowPeak -- optimal overlap narrowPeaks 
* idr.optimal.narrowPeak -- idr narrowPeaks 
* qc.html.txt -- qc html files 
* qc.json.txt -- qc json files 


## augmented files for bpnet ## 
* ambiguous.optimal.narrowPeak 
  -- Overlap peaks minus IDR peaks + 3 blacklists 

* bamCoverage.aligned.bw
  -- produced with command 
    ```  
    bamCoverage -p16 -v --samFlagExclude 4 -b $cur_bam -o $cur_bam.bw
    ```
* bpnet.5pcounts.minus.txt
* bpnet.5pcounts.plus.txt
* bpnet.5pcounts.unstranded.txt
  -- bpnet count tracks are produced with this script:
     ```
     source activate encode-atac-seq-pipeline
     #non-stranded (can be PE or SE) 
     bamCoverage -p16 -v --binSize 1 --samFlagExclude 780 --Offset 1 1 --minMappingQuality 30 -b $cur_bam -o $cur_bam.bpnet.unstranded.bw
     #forward strand -- assumes SE data
     bamCoverage -p16 -v --binSize 1 --samFlagExclude 796 --Offset 1 1 --minMappingQuality 30 -b $cur_bam -o $cur_bam.bpnet.plus.bw
     #reverse strand -- assumes SE data
     bamCoverage -p16 -v --binSize 1 --samFlagExclude 780 --samFlagInclude 16 --Offset 1 1 --minMappingQuality 30 -b $cur_bam -o $cur_bam.bpnet.minus.bw
    ```

* nodup.5counts.plus.txt
* nodup.5pcounts.minus.txt
  -- 5' counts from the tagAlign -- note these differ from the bpnet counts in that duplicates have been removed and other filters have been applied. 
  produced with command 
  ```
  chromsizes=hg38.chrom.sizes
  #plus strand
  genomeCoverageBed -strand + -5 -bg -i $tagAlign -g $chromsizes > $tagAlign.tmp 
  sort -k1,1 -k2,2n  $tagAlign.tmp >  $tagAlign.counts.plus.bg
  rm $tagAlign.tmp 
  bedGraphToBigWig $tagAlign.counts.plus.bg $chromsizes $tagAlign.counts.plus.bw
  
  #minus strand 
  genomeCoverageBed -strand - -5 -bg -i $tagAlign -g $chromsizes > $tagAlign.tmp
  sort -k1,1 -k2,2n $tagAlign.tmp >  $tagAlign.counts.minus.bg
  rm $tagAlign.tmp 
  bedGraphToBigWig $tagAlign.counts.minnus.bg $chromsizes $tagAlign.counts.minus.bw
  ```

## mitra links to the most-used outputs: ##
* mitra/fc.bigwig.mitra
* mitra/pval.bigwig.mitra
* mitra/idr.optimal.narrowPeak.mitra
* mitra/overlap.optimal.narrowPeak.mitra
* mitra/qc.html.mitra.txt
