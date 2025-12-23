#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 11:45
# @Author  : George
# @File    : 17_shutil_archive.py

# shutil模块的应用,压缩和解压文件
import shutil
import zipfile

# 压缩目录d:/dir1内的全部内容 到 d:/dir2/movies.zip
shutil.make_archive(r"d:/dir2/movies", "zip", r"d:/dir1")

# 解压 d:/dir2/movies.zip 到 d:/dir2/movies 目录
with zipfile.ZipFile(r"d:/dir2/movies.zip", "r") as z:
    z.extractall(r"d:/dir2/movies")


# 压缩文件d:/1.png 和 d:/2.png 到 d:/a.zip
zf = zipfile.ZipFile(r"d:/a.zip", "w")
zf.write(r"d:/1.png")
zf.write(r"d:/2.png")
# 关闭压缩文件
zf.close()