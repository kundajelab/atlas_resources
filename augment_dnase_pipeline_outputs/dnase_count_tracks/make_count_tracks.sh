#!/bin/bash
chromsizes=hg38.chrom.sizes
tagAlign=$1 


#plus strand
/share/PI/euan/apps/bin/genomeCoverageBed -strand + -5 -bg -i $tagAlign -g $chromsizes > $tagAlign.tmp 
sort -k1,1 -k2,2n  $tagAlign.tmp >  $tagAlign.counts.plus.bg
#rm $tagAlign.tmp 
/share/PI/euan/apps/bin/bedGraphToBigWig $tagAlign.counts.plus.bg $chromsizes $tagAlign.counts.plus.bw
#minus strand 
/share/PI/euan/apps/bin/genomeCoverageBed -strand - -5 -bg -i $tagAlign -g $chromsizes > $tagAlign.tmp
sort -k1,1 -k2,2n $tagAlign.tmp >  $tagAlign.counts.minus.bg
#rm $tagAlign.tmp
/share/PI/euan/apps/bin/bedGraphToBigWig $tagAlign.counts.minus.bg $chromsizes $tagAlign.counts.minus.bw
