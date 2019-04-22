#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""

"""

__author__ = 'fishzd'

import xlrd
import xlwt
import json

with open('students.txt', encoding='utf-8') as f:
    student_txt = f.read()

student_book = xlwt.Workbook()
sheet = student_book.add_sheet('sheet1', cell_overwrite_ok=True)


student_dict = json.loads(student_txt)

for row, (num, student_info) in enumerate(student_dict.items()):
    sheet.write(row, 0, num)
    for col, info in enumerate(student_info):
        sheet.write(row, col+1, info)

student_book.save('students.xls')