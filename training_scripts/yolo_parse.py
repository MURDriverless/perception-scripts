'''
Author: Andrew Huang

Description: used to convert MIT open-source dataset .csv labels into darknet .txt label files

Usage:
    Command line arguments to be added
'''

import csv
import json

with open("yolov3-training_all.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for i, row in enumerate(csv_reader):
        if i < 2:
            continue

        if i > 100:
            break
        
        imgName = row[0]
        imgWidth = int(row[2])
        imgHeight = int(row[3])
        img_boxes = []
        for img_box_str in row[5:]:
            if not img_box_str == "":
                img_boxes.append(json.loads(img_box_str))

        # csv is X, Y, H, W
        # yolo mark is X_center, Y_center, W, H

        with open("output\{}.txt".format(imgName[:-4]), "w") as out_file:
            for box in img_boxes:
                out_file.write("0 {0:.6f} {1:.6f} {2:.6f} {3:.6f}\n".format((box[0]+box[3]/2)/imgWidth,
                                                                            (box[1]+box[2]/2)/imgHeight,
                                                                            (box[3])/imgWidth,
                                                                            (box[2])/imgHeight))
