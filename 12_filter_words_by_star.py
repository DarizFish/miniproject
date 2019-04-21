#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 
replace sensitive words by stars.
"""

__author__ = 'fishzd'

import re

words_file = 'filtered_words.txt'
with open(words_file, 'r', encoding='utf-8') as f:
    filter_word_list = re.split(r'\s', f.read())

user_str = input('please input a word:  ')

for word in filter_word_list:
    user_str = user_str.replace(word, '*'*len(word))
print(user_str)

