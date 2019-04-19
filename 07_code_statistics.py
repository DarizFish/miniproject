#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" count code information in a given directory."""

__author__ = 'fishzd'

code_dir = r'.'  # current dir

LANGUAGE = 'python'

def parse_file(file):
    code_line_dict = {'valid code': 0, 'anno code': 0, 'blank line': 0}
    with open(file) as f:
        global f_lines
        f_lines = f.readlines()
        for line in f_lines:
            print(line)
            line = line.strip()
            if line.startswith('#'):
                code_line_dict['anno code'] += 1
            elif not line:
                code_line_dict['blank line'] += 1
            else:
                code_line_dict['valid code'] += 1
        return code_line_dict

def parse_files_in_dir(file_dir):
    pass

if __name__ == '__main__':

    # test parse_file func
    stat = parse_file('addNum.py')
