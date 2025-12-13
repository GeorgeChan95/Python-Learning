#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/13 11:18
# @Author  : George
# @File    : 03_file_write.py

# w 模式打开文件，会直接清空文件
# file = open("d://aaa/1.txt", "w", encoding="UTF-8")
# a 模式打开文件，内容将以追加的模式写入到文件中
file = open("d://aaa/1.txt", "a", encoding="UTF-8")

for i in range(0, 10):
    if i != 9:
        file.write(f"{i}-hello Python\n")
    else:
        file.write(f"{i}-hello Python")

# 关闭文件流
file.close()
