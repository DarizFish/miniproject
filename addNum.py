#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' add a message number to a head sculpture'

__author__ = 'fishzd'


#add a number to a picture
from PIL import Image, ImageDraw, ImageFont
head_img = Image.open(r'C:\Users\12104\OneDrive\desktop\sheep.png')
head_img.show()
input_num = 4
rate = 1/4
def add_num(img, num):

    fnt = ImageFont.load_default()
    size = fnt.getsize(str(num))
    print(size)
    blank_img = Image.new('RGBA', size, (255,255,255,0))

    d = ImageDraw.Draw(blank_img)
    d.text((0, 0), str(num), font=fnt, fill=(255,0,0,128))

    width, height = int(img.width*rate), int(img.height*rate)
    num_img = blank_img.resize((width, height))

    img.paste(num_img, (img.width - width, 0), num_img)

    return img


# out_img = add_num(head_img, input_num)
# out_img.show()

def add_num_byfont(img, num):

    font = ImageFont.truetype(r'C:\Program Files\JetBrains\PyCharm Community Edition 2018.3.5\jre64\lib\fonts\DroidSans.ttf', 30)
    d = ImageDraw.Draw(img)
    d.text((0, 0), str(num), font=font, fill=(255,0,0,128))
    return img

out_img2 = add_num_byfont(head_img, input_num)
out_img2.show()
