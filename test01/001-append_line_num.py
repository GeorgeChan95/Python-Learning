#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 9:12
# @Author  : George
# @File    : 001-append_line_num.py

# 读取b.txt , 给每一行内容加行号

with open("D:\\b.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # list 推导
    lines2 = [line.rstrip() + " #" + str(index) for index, line in zip(range(1, len(lines) + 1), lines)]
    print(lines2)

with open("D:\\b.txt", "w", encoding="utf-8") as f:
    for line in lines2:
        f.write(line + "\n")
