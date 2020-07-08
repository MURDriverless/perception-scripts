'''
Author: Steven Lee

Script to remove false positive labels.
    0 - blue
    1 - orange
    2 - yellow
    3 - false positive          <- to be removed

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

    labels = [f for f in listdir(args.label_path)
              if isfile(join(args.label_path, f))]

    fp_cleaned = 0

    for idx, label in enumerate(labels):

        lpath = args.label_path + label
        with open(lpath, "r") as f:
            lines = f.readlines()
        
        with open(lpath, 'w') as f:
            for line in lines:
                if line.strip()[0] != '3':
                    f.write(line)
                else:
                    fp_cleaned += 1

    print("False positives cleaned = ", fp_cleaned)