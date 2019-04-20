#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" parse a html file, and find its body, which can be see on browser. """

__author__ = 'fishzd'

import re

html_file = r'test_htmls\test_zhihu.html'


def remove_tag(html):
    get_all_body = re.search(r'<body.*?>.*?</body>', html, re.DOTALL)
    if get_all_body:
        body = get_all_body.group()
        body = re.sub(r'<script.*?>.*?</script>', ' ', body, flags=re.DOTALL)
        body = re.sub(r'<style.*?>.*?</style>', ' ', body, flags=re.DOTALL)
        body_content = re.sub(r'".*?"', ' ', body)
        body_content1 = re.sub(r'<[^<>]+?>', ' ', body_content)
        body_content2 = re.sub(r'<[^<>]+?>', ' ', body_content1)
        body_content3 = re.sub(r'\n\s*\n', '\n', body_content2, flags=re.MULTILINE)
        return body_content3
    else:
        return 'there is no body in this html file'


def parse_file(file):
    with open(file, encoding='utf-8') as f:
        html = f.read()
        return remove_tag(html)


if __name__ == '__main__':
    html_cont = parse_file(html_file)
    print(html_cont)
