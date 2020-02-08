desired_region_size=5000
flank=2500
outf=open("make_plot.sh",'w')
bl1=open('hg38.blacklist.bed','r').read().strip().split('\n')
for line in bl1:
    tokens=line.split('\t')
    chrom=tokens[0]
    start=int(tokens[1])
    end=int(tokens[2])
    size=end-start
    if size < desired_region_size:
        center=(start+end)/2
        updated_start=int(round(center-flank))
        updated_end=int(round(center+flank))
    else:
        updated_start=start-10
        updated_end=end+10
    outf.write(' '.join(["pyGenomeTracks","--tracks","tracks.ini","--region",chrom+":"+str(updated_start)+'-'+str(updated_end),"--outFileName","bl1."+chrom+":"+str(start)+"_"+str(end)+".pdf"])+'\n')

bl2=open('hg38-blacklist.v2.bed','r').read().strip().split('\n')
for line in bl2:
    tokens=line.split('\t')
    chrom=tokens[0]
    start=int(tokens[1])
    end=int(tokens[2])
    size=end-start
    if size < desired_region_size:
        center=(start+end)/2
        updated_start=int(round(center-flank))
        updated_end=int(round(center+flank))
    else:
        updated_start=start-10
        updated_end=end+10
    outf.write(' '.join(["pyGenomeTracks","--tracks","tracks.ini","--region",chrom+":"+str(updated_start)+'-'+str(updated_end),"--outFileName","bl2."+chrom+":"+str(start)+"_"+str(end)+".pdf"])+'\n')

bl3=open('peakPass60Perc_sorted.bed','r').read().strip().split('\n')
for line in bl3:
    tokens=line.split('\t')
    chrom=tokens[0]
    start=int(tokens[1])
    end=int(tokens[2])
    size=end-start
    if size < desired_region_size:
        center=(start+end)/2
        updated_start=int(round(center-flank))
        updated_end=int(round(center+flank))
    else:
        updated_start=start-10
        updated_end=end+10
    outf.write(' '.join(["pyGenomeTracks","--tracks","tracks.ini","--region",chrom+":"+str(updated_start)+'-'+str(updated_end),"--outFileName","peakPass60Perc."+chrom+":"+str(start)+"_"+str(end)+".pdf"])+'\n')


