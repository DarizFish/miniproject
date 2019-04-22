#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
transform a json file to excel file according to the data structure of json.
"""

__author__ = 'fishzd'

import xlwt
import json
import os

json_file_list = ['numbers.txt', 'students.txt', 'city.txt']


def json2excel(json_file):
    with open(json_file, encoding='utf-8') as f:
        json_txt = f.read()

    data = json.loads(json_txt)

    data_book = xlwt.Workbook()
    sheet = data_book.add_sheet('sheet1', cell_overwrite_ok=True)

    if isinstance(data, dict):
        for row, (key, value) in enumerate(data.items()):
            sheet.write(row, 0, key)
            if isinstance(value, list):
                for col, info in enumerate(value):
                    sheet.write(row, col + 1, info)
            else:
                sheet.write(row, 1, value)
    elif isinstance(data, list):
        for row, num_list in enumerate(data):
            for col, num in enumerate(num_list):
                sheet.write(row, col, num)

    data_book.save(os.path.splitext(json_file)[0] + '.xls')


for file in json_file_list:
    json2excel(file)
