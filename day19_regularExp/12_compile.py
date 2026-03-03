#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/3 18:23
# @Author  : George
# @File    : 12_compile.py

# compile 函数用于编译正则表达式，生成一个正则表达式（Pattern ）对象，
# 供 match() 和 search() 这两个函数使用。语法格式为：
# re.compile(pattern[, flags])
'''
pattern 一个字符串形式的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，
'''
import re

str = 'one1 two2 3 4_'
pattern = r'\w+' # 匹配至少一个字母或数字
regex = re.compile(pattern)
print(regex.search(str)) # <re.Match object; span=(0, 4), match='one1'>
print(re.search(pattern, str)) # <re.Match object; span=(0, 4), match='one1'>