#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
generate a veri_key picture,
with random color point background,
random alphabet,
and blur filter mask
"""

__author__ = 'fishzd'

from PIL import Image, ImageFont, ImageColor, ImageDraw, ImageFilter
import random
import string


def rnd_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


upcase = string.ascii_uppercase
key_list = random.sample(upcase, 4)
height = 80
width = 4 * height
key_img = Image.new('RGB', size=(width, height))

draw = ImageDraw.Draw(key_img)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())

fnt = ImageFont.truetype(r'C:\Windows\Fonts\msyhbd.ttc', 50)
for index, key in enumerate(key_list):
    draw.text((15 + height * index, 5), key, font=fnt, fill=random.choice(list(ImageColor.colormap)))

key_img = key_img.filter(ImageFilter.GaussianBlur(2))

key_img.save('veri_key.jpg')
