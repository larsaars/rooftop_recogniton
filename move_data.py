"""
move all unlabelled data to test_images dir
"""

import os
from os.path import join, exists

labels_dir, train_images_dir, test_images_dir = './labels', './train_images',  './test_images'

for image_name in os.listdir(train_images_dir):
    if not exists(join(labels_dir, image_name)):
        os.rename(join(train_images_dir, image_name), join(test_images_dir, image_name))


