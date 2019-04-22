#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import xlrd
import xml.dom.minidom

students_excel = xlrd.open_workbook('students.xls')

sheet = students_excel.sheet_by_index(0)

students_dict = {}

for row in range(0, sheet.nrows):
    students_dict[sheet.cell(row, 0).value] = []
    for col in range(1, sheet.ncols):
        students_dict[sheet.cell(row, 0).value].append(sheet.cell(row, col).value)

doc = xml.dom.minidom.Document()
root = doc.createElement('root')
doc.appendChild(root)

stu_comment = doc.createComment('\n\t学生信息表 	\n\t"id" : [名字, 数学, 语文, 英文]\n')
stu_str = '{\n%s\n}' % ',\n'.join(['\t"%s" : %s' % (key, value) for key, value in students_dict.items()])

student_node = doc.createElement('student')
student_node.appendChild(stu_comment)
student_node.appendChild(doc.createTextNode(stu_str))
root.appendChild(student_node)

with open('students.xml', 'w', encoding='utf-8') as fp:
    doc.writexml(fp, indent='', addindent='', newl='\n', encoding="utf-8")
