#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/13 14:24
# @Author  : George
# @File    : 04_file_delete.py
import os.path

if os.path.exists("d://aaa//1.txt"):
    os.remove("d://aaa//1.txt")
else:
    print("文件不存在")