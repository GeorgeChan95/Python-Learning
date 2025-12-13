#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/13 10:09
# @Author  : George
# @File    : 01_file_create.py

file = open("d://aaa//1.txt", "w", encoding="UTF-8") # 如果 aaa 目录不存在，文件创建失败，不是自动创建父文件夹

print(f"文件创建成功，类型是：{type(file)}") # 文件创建成功，类型是：<class '_io.TextIOWrapper'>