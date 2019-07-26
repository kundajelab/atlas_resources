import pandas as pd 
import argparse 
def parse_args(): 
    parser=argparse.ArgumentParser(description="generate pipeline input jsons")
    parser.add_argument("--bam_name_to_location") 
    parser.add_argument("--experiments_metadata") 
    parser.add_argument("--pipeline_json_dir")
    parser.add_argument("--pipeline_output_dir") 
    parser.add_argument("--caper_submit_script") 
    return parser.parse_args() 

def main(): 
    args=parse_args() 
    

if __name__=="__main__": 
    main() 

