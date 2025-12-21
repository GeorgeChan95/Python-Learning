#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 10:46
# @Author  : George
# @File    : 11_csv_read_write.py

# csv文件的读写操作
import csv

# csv 文件的读取
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


# csv 文件的写入
headers = ["工号","姓名","年龄","地址","月薪"]
rows = [("1001","高淇",18,"西三旗1号院","50000"),("1002","高八",19,"西三旗1号院","30000")]
with open(r"test2.csv", "w", encoding="utf-8", newline='') as f2: # newline='' 去除行与行之间的换行符
    w_f2 = csv.writer(f2)
    w_f2.writerow(headers)
    w_f2.writerows(rows)