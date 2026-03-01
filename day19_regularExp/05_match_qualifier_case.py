#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/1 11:50
# @Author  : George
# @File    : 04_match_qualifier.py

# 限定符的案例测试
import re

'''
*       匹配零次或多次
+       匹配一次或多次
?       匹配一次或零次
{m}     重复m次
{m,n}   重复m到n次，其中n可以省略，表示m到任意次
{m,}    至少m次
'''


# 匹配出一个字符串首字母为大写字符，后边都是小写字符，这些小写字母可有可无
pattern = '[A-Z][a-z]*'
str = 'Abc' # <re.Match object; span=(0, 3), match='Abc'>
str = 'B' # <re.Match object; span=(0, 1), match='B'>
str = 'ge' # None
print(re.match(pattern, str))