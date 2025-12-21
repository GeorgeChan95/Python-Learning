#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 10:46
# @Author  : George
# @File    : 11_csv_read_write.py

# csv文件的读写操作
import csv

with open(r"d:/test.csv") as f:
    cf = csv.reader(f)
    header = next(cf)
    print(f"表头内容：{header}") # 表头内容：['姓名', '年龄', '身高', '体重']
    data_list = list(cf)
    for rowNum in range(0, len(data_list)):
        print(f"第：{rowNum}行内容：{data_list[rowNum]}")

'''
表头内容：['姓名', '年龄', '身高', '体重']
第：0行内容：['何飞', '20', '180', '80']
第：1行内容：['戴璐', '22', '160', '50']
第：2行内容：['江青', '18', '180', '88']
'''