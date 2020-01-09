#50
for i in `seq 0 14`
do
    python make_xml_session.py --paths 50/x$i --outf 50/atlas.pval.bigwigs.50.$i.xml
done

#100
for i in `seq 0 7`
do
    python make_xml_session.py --paths 100/x$i --outf 100/atlas.pval.bigwigs.100.$i.xml
done


#200
for i in `seq 0 3`
do
    python make_xml_session.py --paths 200/x$i --outf 200/atlas.pval.bigwigs.200.$i.xml
done

#400 
for i in `seq 0 1`
do
    python make_xml_session.py --paths 400/x$i --outf 400/atlas.pval.bigwigs.400.$i.xml
done

#all
python make_xml_session.py --paths pval_mitra_paths.txt --outf atlas.pval.bigwigs.all.xml

