#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 9:46
# @Author  : George
# @File    : 002_img_copy.py

# 实现二进制文件内容的拷贝
with open("d:\\1.png", "rb") as sourceF, open("d:\\11.png", "wb") as targetF:
    for sour in sourceF: # 从源文件读取数据，往目标文件写
        targetF.write(sour)