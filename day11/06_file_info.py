#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/13 15:03
# @Author  : George
# @File    : 06_file_info.py
import os
import time

file_info = os.stat("D://aaa//1.txt")
print("--------文件信息---------")
print(f"文件大小：{file_info.st_size} 字节\n"
      f"最近访问时间：{time.ctime(file_info.st_atime)}\n"
      f"文件创建时间：{time.ctime(file_info.st_ctime)}\n"
      f"文件修改时间：{time.ctime(file_info.st_mtime)}")
'''
--------文件信息---------
文件大小：8 字节
最近访问时间：Sat Dec 13 15:04:22 2025
文件创建时间：Sat Dec 13 15:04:10 2025
文件修改时间：Sat Dec 13 15:04:21 2025
'''