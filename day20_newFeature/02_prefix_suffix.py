#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 18:55
# @Author  : George
# @File    : 02_prefix_suffix.py

# 字符串前缀和后缀的处理
str = 'hello world'
# 移除前缀
print(str.removeprefix('hell')) # o world
str = 'hello world hello'
print(str.removeprefix('hello')) #  world hello

# 移除后缀
print(str.removesuffix('llo')) # hello world he
