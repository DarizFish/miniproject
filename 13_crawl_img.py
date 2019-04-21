#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 
crawl img from target url.
notice: the html page should be static.
"""

__author__ = 'fishzd'

import re
from PIL import Image
import requests
from io import BytesIO
import os

target_url = 'http://tieba.baidu.com/p/2166231880'
anime_url = 'https://www.enterdesk.com/special/dongmantupian/'
saved_dir = 'saved_imgs'


def next_name():
    li = [1]

    def counter():
        li[0] += 1
        return str(li[0])

    return counter


next_id = next_name()


def url2img(src_url):
    if src_url.startswith('//'):
        src_url = 'http:' + src_url
    try:
        r = requests.get(src_url)
        i = Image.open(BytesIO(r.content))
        return i
    except Exception as e:
        print(e)
    finally:
        pass


def crawl_url_img(url):
    r = requests.get(url)
    html = r.text
    src_urls = re.findall(r'<img.*?src="(.*?)".*?>', html, flags=re.DOTALL)
    src_urls = sorted(set(src_urls), key=src_urls.index)
    img_list = [url2img(u) for u in src_urls]
    return img_list


if __name__ == '__main__':
    url_imgs = crawl_url_img(anime_url)
    for img in url_imgs:
        if img:
            img.save(os.path.join(saved_dir, next_id() + '.png'), format='PNG')
