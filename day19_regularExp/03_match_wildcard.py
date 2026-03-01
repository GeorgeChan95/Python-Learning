#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/1 11:08
# @Author  : George
# @File    : 03_match_wildcard.py

# match 函数常用匹配符

# . 匹配任意一个字符（除了 \n）
# [] 匹配列表中的字符
# \w 匹配字母、数字、下划线，即 a-z,A-Z,0-9,_
# \W 匹配不是字母、数字、下划线
# \s 匹配空白字符,即空格(\n,\t)
# \S 匹配不是空白的字符
# \d 匹配数字,即 0-9
# \D 匹配非数字的字符

import re

#常用匹配符  . 使用 匹配任意一个字符除了(\n)
pattern = "."
str = '9'
str = 'a'
str = 'B'
str = '_'
#定义目标式 \n
str = '\n' # None
# print(re.match(pattern, str))


# 常用匹配符 \d 匹配数字
str = '0'
str = '9'
str = 'a' # None
str = '_' # None
str = 'B' # None
pattern = r'\d'
# print(re.match(pattern, str))


# \D 匹配非数字
pattern = r'\D'
str = 'a'
str = '-'
str = '0' # None
# print(re.match(pattern, str))


# \s 匹配空白字符,即空格(\n,\t)
str = ' '
str = '\n'
str = '\t'
str = 'a' # None
str = '-' # None
pattern = r'\s'
# print(re.match(pattern, str))

# \S 匹配不是空白的字符
str = ' ' # None
str = '\n' # None
str = '\t' # None
str = 'a'
str = '-'
pattern = r'\S'
# print(re.match(pattern, str))


# \w 匹配字母、数字、下划线，即 a-z,A-Z,0-9,_
str = ' ' # None
str = '\n' # None
str = '\t' # None
str = 'a'
str = '-' # None
str = '_'
str = '@' # None
str = '1'
pattern = r'\w'
# print(re.match(pattern, str))


# \W 匹配不是字母、数字、下划线
str = ' '
str = '\n'
str = '\t'
str = 'a' # None
str = '-'
str = '_' # None
str = '@'
str = '1' # None
pattern = r'\W'
# print(re.match(pattern, str))


# [] 匹配列表中的字符
str = ' ' # None
str = '\n'
str = '\t' # None
str = 'a'
str = '-' # None
str = '_'  # None
str = '@'  # None
str = '1'
pattern = r'[13579a\n]'
# print(re.match(pattern, str))

# 匹配手机号码
pattern = r'1[35789]\d\d\d\d\d\d\d\d\d'
str = '18327890987'
str = '327890987' # None
str = '01327890987' # None
print(re.match(pattern, str))