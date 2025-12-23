#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 11:53
# @Author  : George
# @File    : 19_recurse_dir.py
import os


# 递归遍历目录,并打印所有文件路径

def print_dir(path, indent=0):
    # 打印当前目录路径
    # 遍历当前目录下的所有文件和子目录
    child_file = os.listdir(path)
    for file in child_file:
        f = os.path.join(path, file)
        print(f"目录层级：{indent}, 路径：{f}")
        if os.path.isdir(f):
            print_dir(f, indent+1)

print_dir(r"D:\dir2", 0)