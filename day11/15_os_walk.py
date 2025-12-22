#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 11:39
# @Author  : George
# @File    : 15_os_walk.py
import os

# os模块的应用,walk遍历目录
path = os.getcwd() # 当前工作路径
print(f"当前工作路径：{path}") # E:\study\PythonLearning\Python-Learning\day11

# root：当前遍历的目录路径（字符串）
# dirs：root 目录下的所有子目录名（列表，仅包含目录名，不含路径）。
# files：root 目录下的所有文件名（列表，仅包含文件名，不含路径）。
# 参数 topdown=False：指定遍历方向为自底向上（默认 topdown=True 为自顶向下）。即先遍历最深层的子目录，再逐步向上遍历到顶层目录 path。
list_files = os.walk(path, topdown=False)
for root, dirs, files in list_files:
    for name in files:
        # os.path.join(root, name)：将目录路径 root 与文件名 name 拼接，生成文件的完整绝对路径（避免手动拼接路径时因操作系统差异导致的错误，如 Windows 使用 \，Linux/macOS 使用 /）。
        print(os.path.join(root, name))
    print("-------------------------------------")
    for name in dirs:
        print(os.path.join(root, name))