#conversion of annotations from yml to txt

import numpy as np
import os
import ruamel.yaml as yaml

#range for the entire dataset, sets for the picked ones
#obj_ids = range(1, 31)
obj_ids = range(0,5)

cwd = os.getcwd()
data_path = os.path.join(cwd, 'data/t-less_v2')

#choose entire set or just the picked objects
#obj_gt_path_mask = os.path.join(data_path, 'test_primesense', '{:02d}', 'gt.yml')
#folder_path =  os.path.join(data_path, 'test_primesense', '{:02d}','rgb','{:04d}.png')
obj_gt_path_mask = os.path.join(data_path, 'train_primesense_pick', '{:02d}', 'gt.yml')
folder_path =  os.path.join(data_path, 'train_primesense_pick', '{:02d}','rgb','{:04d}.png')


def load_gt(path):
    with open(path, 'r') as f:
        gts = yaml.load(f, Loader=yaml.CLoader)
        for im_id, gts_im in gts.items():
            for gt in gts_im:
                if 'obj_bb' in gt.keys():
                    gt['obj_bb'] = [int(x) for x in gt['obj_bb']]
                    gt['obj_bb'] = [gt['obj_bb'][0], gt['obj_bb'][1], gt['obj_bb'][0] + gt['obj_bb'][2], gt['obj_bb'][1]+gt['obj_bb'][3]]

                    gts[im_id] = gt['obj_bb']

    return gts

for obj_id in obj_ids:

    #loading info of images
    obj_gt_path = obj_gt_path_mask.format(obj_id)
    object_gt = load_gt(obj_gt_path)

    for i in object_gt:
        #choose one of the text files based on the dataset.
        text_file = open("t-less-annotations_pick.txt", "a+")
        #text_file = open("t-less-annotations-single.txt", "a+")
        text_file.write(', '.join([folder_path.format(obj_id,i) + ' ' + ','.join(map(str, object_gt[i]))+','+str(obj_id)]) + '\n')
        text_file.close()
        #print(str(folder_path.format(obj_id)) + ' ,'.join(map(str,object_gt[i])) + i)
