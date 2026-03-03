#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/3 18:23
# @Author  : George
# @File    : 13_findall.py
import re

# findall 函数
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，
# 如果没有找到匹配的，则返回空列表。语法格式如下：
# findall(pattern, string, flags=0)

s = 'one1 two2 3 4_'
pattern = r'\w+'
print(re.findall(pattern, s)) # ['one1', 'two2', '3', '4_']
print(re.search(pattern, s)) # <re.Match object; span=(0, 4), match='one1'>