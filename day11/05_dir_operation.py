#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/13 14:39
# @Author  : George
# @File    : 05_dir_operation.py
import os

# 1、创建单个目录
if not os.path.isdir("D://aaa"):
    os.mkdir("D://aaa")
    print("D://aaa 目录创建成功")
else:
    print("D://aaa 目录已存在")


# 2、创建多级目录
if not os.path.isdir("D://bbb//ccc"):
    os.makedirs("D://bbb//ccc", mode=0o777, exist_ok=True) # exist_ok=True 表示目录已存在，创建也不会报错
    print("多级目录：D://bbb//ccc 创建成功")
else:
    print("多级目录：D://bbb//ccc 已存在")


# 3、删除单个目录
if os.path.isdir("D://aaa"):
    os.rmdir("D://aaa")
    print("删除单层目录：D://aaa 操作成功")
else:
    print("目录：D://aaa 不存在，无需删除")


# 4、删除多级目录
if os.path.isdir("D://bbb//ccc"):
    os.removedirs("D://bbb//ccc")
    print("删除多级目录：D://bbb//ccc 操作成功")
else:
    print("目录：D://bbb//ccc 不存在，无需删除")