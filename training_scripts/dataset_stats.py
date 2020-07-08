'''
Author: Steven Lee

Script to generate basic stats about a yolo dataset.
Generate a count of all the different classes present in the dataset.
    0 - blue
    1 - orange
    2 - yellow
    3 - false positive

Usage:
    python3 yolo_check.py /path/to/label/
'''

import csv
import json
import os
import shutil
import sys
import argparse
import math

from pathlib import Path
from os import listdir
from os.path import isfile, join


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('label_path', type=str,
                        help='path to the label files')

    args = parser.parse_args()
    
    
    labels = [f for f in listdir(args.label_path) if isfile(join(args.label_path, f))]
    
    blue = 0
    orange = 0
    yellow = 0
    fp = 0
    
    for idx, label in enumerate(labels):
        
        # if idx > 10:
        #     break
        
        lpath = args.label_path + label
        with open(lpath, "r") as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            
            for line in lines:
                if line[0] == '0':
                    blue += 1
                elif line[0] == '1':
                    orange += 1
                elif line[0] == '2':
                    yellow += 1
                elif line[0] == '3':
                    fp += 1
    
    print('Dataset Statistics:')
    print('blue   = ', blue)
    print('orange = ', orange)
    print('yellow = ', yellow)
    print('fp     = ', fp)