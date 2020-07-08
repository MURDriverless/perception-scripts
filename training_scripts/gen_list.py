'''
Author: Steven Lee

Description: generate train.txt and valid.txt from provided csv files

Usage:
    python3 yolo_parse.py /path/to/train/csv /path/to/valid/csv
    
Note that the outputs will be dumped in a `output` folder in the working directory
'''

import csv
import json

import os
import shutil
import sys
import argparse
import math
from pathlib import Path

def generate_txt_list(csv_path, output_name):
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        os.makedirs("output", exist_ok=True)

        with open('./output/{}'.format(output_name), 'w') as out_file:
            for i, row in enumerate(csv_reader):
                if i < 2:
                    continue
                
                imgName = row[0]
                ds_path = '/work/dataset/YOLO_Dataset/'
                out_file.write(ds_path + imgName + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('train_csv_path', type=str,
                        help = 'path to the train csv file')
    parser.add_argument('valid_csv_path', type=str,
                        help = 'path to the valid csv file')
    
    args = parser.parse_args()

    generate_txt_list(args.train_csv_path, 'train.txt')
    generate_txt_list(args.valid_csv_path, 'valid.txt')
