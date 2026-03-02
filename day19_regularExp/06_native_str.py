#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/2 11:18
# @Author  : George
# @File    : 06_native_str.py

# 原生字符串
import re

s = 'c:\\a\\c'
print(s) # c:\a\c
#反斜杠作为转义
s = '\n123'
print(s)
'''

123
'''
s = '\\n123'
print(s) # \n123
#使用原生字符串 r
s = r'\n123'
print(s) # \n123


#在正则表达式中反斜杠作为转义
s = '\n123'
# pattern = '\n\d{3}'
# print(re.match(pattern,s)) # SyntaxWarning: invalid escape sequence '\d' pattern = '\n\d{3}'

#使用原生字符串
# s = '\\n123'
s = '\\\\n123'
pattern = r'\\\\n\d{3}'
print(re.match(pattern,s))