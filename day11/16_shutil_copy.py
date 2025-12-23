#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 11:43
# @Author  : George
# @File    : 16_shutil_copy.py
import os.path
# shutil模块的应用,复制文件
import shutil

# 复制文件
shutil.copyfile(r"d:/test.csv", r"d:/test2.csv")

# 复制目录,如果 dir2 已存在则忽略
shutil.copytree(r"d:/dir1", r"d:/dir2", ignore=shutil.ignore_patterns("*.png"), dirs_exist_ok=True)


res = os.path.exists("d:/dir2")
print(f"目录d:/dir2是否存在：{res}")

# 删除目录
shutil.rmtree(r"d:/dir2")

# 删除文件
os.remove("d:/test2.csv")
