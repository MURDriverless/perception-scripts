'''
Author: Steven Lee

This scripts swaps the width and height parameters in the label files.
This should ONLY be used in the event where the width and height of the labels
are swapped around.

<object-class> <x_center> <y_center> <width> <height>

If you are reading this and you are planning to use this, then you might have
done something very wrong. If you have trained a model using swapped width and
height then you have my condolences.

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

    swapped = 0

    for idx, label in enumerate(labels):

        lpath = args.label_path + label
        with open(lpath, "r") as f:
            lines = f.readlines()
        
        with open(lpath, 'w') as f:
            for line in lines:
                line = line.rstrip().split(' ')
                w = line[4]
                h = line[3]
                line[3] = w
                line[4] = h
                new_label = ' '.join(x for x in line) + '\n'
                f.write(new_label)
        
        swapped += 1
    
    print("Swapped ", swapped, " labels.")