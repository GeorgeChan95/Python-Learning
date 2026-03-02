#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/2 19:55
# @Author  : George
# @File    : 08_search.py
import re

# search 函数的使用
# search在一个字符串中搜索满足文本模式的字符串。
# 语法格式如下：
# re.search(pattern, string, flags=0)

# match与search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。

pattern = 'hello'
str = 'hi hello py'
print(re.match(pattern, str)) # None
print(re.search(pattern, str)) # <re.Match object; span=(3, 8), match='hello'>