#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 10:45
# @Author  : George
# @File    : 09_seek_tell.py

# 文件的指针操作
with open("e.txt", "r", encoding="utf-8") as f:
    print(f"文件名：{f.name}") # 文件名：e.txt
    print(f"当前指针的位置：{f.tell()}") # 当前指针的位置：0
    print(f.readline()) # 打印一行内容
    print(f"当前指针的位置：{f.tell()}") # 当前指针的位置：9
    # 因此，f.seek(3, 0) 的整体作用是：将文件指针从文件开头向后移动 3 个字节，并返回新的指针位置（此处返回值为 3，
    # 所以 print 语句会输出 3）。后续对文件的读取（如 read()、readline() 等）将从这个新位置开始。
    f.seek(3, 0)
    print(f.readline()) # 4567
