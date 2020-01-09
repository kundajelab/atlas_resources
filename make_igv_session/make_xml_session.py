#generate html web page to visualize the SNP interpretations
import argparse 
from xml.etree import ElementTree as ET
from xml.dom import minidom
from io import BytesIO

def parse_args():
    parser=argparse.ArgumentParser(description="generate igv session from list of bigwigs")
    parser.add_argument("--paths")
    parser.add_argument("--outf")
    return parser.parse_args()

def make_session():
    session=ET.Element("Session")
    session.set('genome','hg38')
    session.set('hasGeneTracks','true')
    session.set('hasSequenceTrack','true')
    session.set('locus','chr3:24704067-26618414')
    session.set('nextAutoScaleGroup','5')
    session.set("path","C:\\Users\\Anshul\\Desktop\\igv_session.xml")
    session.set("version","8") 
    return session

def main():
    args=parse_args()
    paths=open(args.paths,'r').read().strip().split('\n')
    session=make_session()
    resources=ET.SubElement(session,'Resources')
    for path in paths:
        resource=ET.SubElement(resources,'Resource')
        resource.set("path",path)
    data_panel=ET.SubElement(session,"Panel")
    data_panel.set("height","698")
    data_panel.set("name","DataPanel")
    data_panel.set("width","1901")
    for path in paths:
        track=ET.SubElement(data_panel,'Track')
        track.set('autoScale','False')
        track.set('autoScaleGroup','4')
        track.set('clazz',"org.broad.igv.track.DataSourceTrack")
        track.set('fontSize','10')
        track.set('id',path)
        basename=path.split('/')[-1].split('.')[0]
        track.set('name',basename)
        track.set('renderer','BAR_CHART')
        track.set('visible','true')
        track.set('windowFunction','max')
        data_range=ET.SubElement(track,'DataRange')
        data_range.set('baseline','0.0')
        data_range.set('drawBaseline','true')
        data_range.set('flipAxis','false')
        data_range.set('maximum','67')
        data_range.set('minimum','0')
        data_range.set('type','linear')
    feature_panel=ET.SubElement(session,'Panel')
    feature_panel.set('height','99')
    feature_panel.set('name','FeaturePanel')
    feature_panel.set('width','1901')
    ref_seq_track=ET.SubElement(feature_panel,'Track')
    ref_seq_track.set('clazz','org.broad.igv.track.SequenceTrack')
    ref_seq_track.set('fontSize','10')
    ref_seq_track.set('id','Reference sequence')
    ref_seq_track.set('name','Reference sequence')
    ref_seq_track.set('visible','true')
    ref_gene_track=ET.SubElement(feature_panel,'Track')
    ref_gene_track.set('clazz','org.broad.igv.track.FeatureTrack')
    ref_gene_track.set('color','0,0,178')
    ref_gene_track.set('colorScale','ContinuousColorScale;0.0;426.0;255,255,255;0,0,178')        
    ref_gene_track.set('fontSize','10')
    ref_gene_track.set('height','35')
    ref_gene_track.set('id','hg38_genes')
    ref_gene_track.set('name','Gene')
    ref_gene_track.set('visible','true')
    panel_layout=ET.SubElement(session,'PanelLayout')
    panel_layout.set("dividerFractions","0.87")
    hidden_attributes=ET.SubElement(session,'HiddenAttributes')
    data_file_attribute=ET.SubElement(hidden_attributes,"Attribute")
    data_file_attribute.set("name","DATA FILE")
    data_type_attribute=ET.SubElement(hidden_attributes,"Attribute")
    data_type_attribute.set("name","DATA TYPE")
    name_attribute=ET.SubElement(hidden_attributes,"Attribute")
    name_attribute.set("name","NAME")

    #write output
    session_tree=ET.ElementTree(session)
    f=BytesIO()
    session_tree.write(f,encoding='utf-8',xml_declaration=True)
    session_string=f.getvalue()
    reparsed=minidom.parseString(session_string).toprettyxml(indent="\t")
    
    
    #session_string=ET.tostring(session,method='xml',encoding='utf-8').decode()
    with open(args.outf,'w') as f:
        #print(session_string)
        f.write(reparsed)
        
    
if __name__=="__main__":
    main()
    
