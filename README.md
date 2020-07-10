# Perception Scripts

Contains scripts which are used to check and pre-process darknet YOLO datasets.

```
training_scripts
├── dataset_cleanup.py      (removes false positive labels)
├── dataset_stats.py        (generates basic dataset stats)
├── dataset_swap_wh.py      (swap width height within labels)
├── gen_list.py             (generates train.txt and valid.txt for training)
├── yolo_check.py           (check if all images and labels are present)
└── yolo_parse.py           (generates labels from csv)
```
