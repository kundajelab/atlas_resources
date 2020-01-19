#bigwig_type=pval
bigwig_type=frombam

#50
for i in `seq 0 14`
do
    python make_xml_session.py --paths $bigwig_type\_inputs/50/x$i --outf $bigwig_type\_inputs/50/atlas.$bigwig_type.bigwigs.50.$i.xml
done

#100
for i in `seq 0 7`
do
    python make_xml_session.py --paths $bigwig_type\_inputs/100/x$i --outf $bigwig_type\_inputs/100/atlas.$bigwig_type.bigwigs.100.$i.xml
done


#200
for i in `seq 0 3`
do
    python make_xml_session.py --paths $bigwig_type\_inputs/200/x$i --outf $bigwig_type\_inputs/200/atlas.$bigwig_type.bigwigs.200.$i.xml
done

#400 
for i in `seq 0 1`
do
    python make_xml_session.py --paths $bigwig_type\_inputs/400/x$i --outf $bigwig_type\_inputs/400/atlas.$bigwig_type.bigwigs.400.$i.xml
done

#all
python make_xml_session.py --paths $bigwig_type\_inputs/$bigwig_type\_mitra_paths.txt --outf $bigwig_type\_inputs/atlas.bigwigs.all.xml

