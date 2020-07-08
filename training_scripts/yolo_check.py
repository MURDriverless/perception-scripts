'''
Author: Steven Lee

Modified from the yolo_parse.py script which checks if all the images and 
labels are ready for training.

Usage:
    python3 yolo_check.py /path/to/csv/file /path/to/img/ /path/to/label/
    
    For example
    python3 yolo_check.py yolov3-training_all.csv YOLO_Dataset/ frames/

'''

import csv
import json
import os
import shutil
import sys
import argparse
import math
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('csv_path', type=str,
                        help='path to the csv file')
    parser.add_argument('img_path', type=str,
                        help='path to the image data')
    parser.add_argument('label_path', type=str,
                        help='path to the label files')

    args = parser.parse_args()

    with open(args.csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for i, row in enumerate(csv_reader):
            if i < 2:
                continue

            # if i > 30:
            #     break

            imgName = row[0]
            labelName = row[0].split(".")[0] + ".txt"
            imgWidth = int(row[2])
            imgHeight = int(row[3])
            img_boxes = []
            for img_box_str in row[5:]:
                if not img_box_str == "":
                    img_boxes.append(json.loads(img_box_str))

            imgPath = args.img_path + imgName
            labelPath = args.label_path + labelName
            
            if not os.path.exists(imgPath):
                print("missing image " + imgPath)
            if not os.path.exists(labelPath):
                print("missing label " + labelPath)
    print("all images and labels exist!")
