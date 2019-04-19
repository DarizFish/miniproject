#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" count code information in a
    given directory."""

__author__ = 'fishzd'

import os

code_dir = r'.'  # current dir

LANGUAGE = 'python'

def parse_file(file):
    code_line_dict = {'valid code': 0, 'anno code': 0, 'blank line': 0}
    with open(file, encoding='utf-8') as f:
        global f_lines
        f_lines = f.readlines()
        doc_anno = False
        for line in f_lines:
            # print(line)
            line = line.strip()
            if line.startswith('"""'):
                doc_anno = True

            if not line:
                code_line_dict['blank line'] += 1
            elif line.startswith('#') or doc_anno:
                code_line_dict['anno code'] += 1
            else:
                code_line_dict['valid code'] += 1

            if line.endswith('"""'):
                doc_anno = False

        return code_line_dict

def parse_files_in_dir(file_dir):
    all_file_list = [os.path.join(file_dir, f) for f in os.listdir(file_dir)]
    code_file_list = list(filter(lambda f: os.path.isfile(f), all_file_list))
    code_file_dict = {}
    for code_file in code_file_list:
        code_file_dict[code_file] = parse_file(code_file)
    return code_file_dict

if __name__ == '__main__':
    code_stat = parse_files_in_dir(code_dir)
    # test parse_file func
    # stat = parse_file('addNum.py')
