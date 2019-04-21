#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 
detect if the user input sensitive words.
sensitive words is stored in a file
"""

__author__ = 'fishzd'

import re

words_file = 'filtered_words.txt'
with open(words_file, 'r', encoding='utf-8') as f:
    filter_word_list = re.split(r'\s', f.read())

user_str = input('please input a word')

sensitive_list = [w in user_str for w in filter_word_list]
print('Freedom') if True in sensitive_list else print('Human Rights')
