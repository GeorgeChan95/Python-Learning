#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 11:47
# @Author  : George
# @File    : 18_zipfile.py

# zipfile模块的应用,压缩和解压文件
import zipfile

# 解压 d:/dir2/movies.zip 到 d:/dir2/movies 目录
with zipfile.ZipFile(r"d:/dir2/movies.zip", "r") as z:
    z.extractall(r"d:/dir2/movies")