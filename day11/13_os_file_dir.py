#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 11:13
# @Author  : George
# @File    : 13_os_file_dir.py

# os模块的应用,操作文件和目录
import os
# 删除目录
# os.rmdir("电影")
# # 创建目录
# os.mkdir("电影")
# os.rmdir("电影")
#
# # 创建多级目录
# os.makedirs("电影/港台/周星驰")

# 返回目录和文件列表
dirs = os.listdir("电影")
print(dirs)

# 遍历目录
files = os.walk("电影")
# 遍历生成器获取目录树信息
for dirpath, dirnames, filenames in files:
    print(f"当前目录路径: {dirpath}")    # 当前遍历到的目录路径
    print(f"子目录列表: {dirnames}")     # 当前目录下的所有子目录名
    print(f"文件列表: {filenames}")      # 当前目录下的所有文件名
    print("-" * 50)  # 分隔线，方便查看不同目录的信息