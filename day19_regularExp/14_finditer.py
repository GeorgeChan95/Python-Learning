#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/3 18:23
# @Author  : George
# @File    : 14_finditer.py

# finditer函数
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

import re

s = 'one1 two2 3 4_'
pattern = r'\w+'
result = re.finditer(pattern, s)
for i in result:
    print(i.group())
''' 打印内容如下：
one1
two2
3
4_
'''