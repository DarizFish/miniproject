#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' adjust a picture to iphone5'

__author__ = 'fishzd'


from PIL import Image
import os
#input should be a directory. then we need to find all the img and change their size.

iphone5 = (500, 1000)

img_dir = r'C:\Users\12104\OneDrive\desktop'

output_dir = r'C:\Users\12104\OneDrive\desktop\iphone5img'

def img_scale(img):
    width_rate = img.width/iphone5[0]
    height_rate = img.height/iphone5[1]
    rate = max(height_rate, width_rate)
    return img.resize((int(img.width/rate), int(img.height/rate)))

def find_all_img(img_dir):
    img_file_list = [os.path.join(img_dir, f) for f in os.listdir(img_dir)]
    img_file_list = list(filter(lambda f: os.path.isfile(f) and os.path.splitext(f)[1] in ['.png', '.jpg'], img_file_list))
    for img_file in img_file_list:
        img = Image.open(img_file)
        output_img = img_scale(img)
        output_img.save(os.path.join(output_dir, os.path.split(img_file)[1]))

if __name__ == '__main__':
    find_all_img(img_dir)
