#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/1 11:50
# @Author  : George
# @File    : 04_match_qualifier.py

# 限定符的使用
import re

'''
*       匹配零次或多次
+       匹配一次或多次
?       匹配一次或零次
{m}     重复m次
{m,n}   重复m到n次，其中n可以省略，表示m到任意次
{m,}    至少m次
'''

# * 匹配零次或多次
str = 'aa'
str = 'b'
str = '1'
str = ' ' # 可以匹配，<re.Match object; span=(0, 0), match=''>， 第一个空格字符，满足 0个单词字符
str = '你' # 可以匹配，python3支持 Unicode，中文也可以支持
str = '%' # <re.Match object; span=(0, 0), match=''>，满足0个字符
str = '@' # <re.Match object; span=(0, 0), match=''>，满足0个字符
pattern = r'\w*' # 匹配 0 个或多个“单词字符”（字母、数字、下划线、Unicode字符（含中文））
# print(re.match(pattern, str))


# + 匹配一次或多次
str = 'aa'
str = 'b'
str = '1'
str = ' ' # None
str = '你' # 可以匹配，python3支持 Unicode，中文也可以支持
str = '%' # None
str = '@' # None
pattern = r'\w+' # 匹配 1个或多个“单词字符”（字母、数字、下划线、Unicode字符（含中文））
# print(re.match(pattern, str))


# ? 匹配一次或零次
str = 'aa'
str = 'b'
str = '1'
str = ' ' # 可以匹配，<re.Match object; span=(0, 0), match=''>， 第一个空格字符，满足 0个单词字符
str = '你' # 可以匹配，python3支持 Unicode，中文也可以支持
str = '%' # 可以匹配，<re.Match object; span=(0, 0), match=''>， 第一个空格字符，满足 0个单词字符
str = '@' # 可以匹配，<re.Match object; span=(0, 0), match=''>， 第一个空格字符，满足 0个单词字符
pattern = r'\w?' # 匹配 1个或0个“单词字符”（字母、数字、下划线、Unicode字符（含中文））
# print(re.match(pattern, str))


# {m} 重复m次
str = 'aa' # <re.Match object; span=(0, 2), match='aa'>
str = 'b' # None
str = '111' # <re.Match object; span=(0, 2), match='11'>
str = ' ' # None
str = '你你' # <re.Match object; span=(0, 2), match='你你'>
str = '%%' # None
str = '@' # None
pattern = r'\w{2}' # 匹配 连续两个单词字符（字母、数字、下划线、Unicode字符（含中文））
# print(re.match(pattern, str))


# {m,n} 重复m到n次，其中n可以省略，表示m到任意次
str = 'aa' # <re.Match object; span=(0, 2), match='aa'>
str = 'b' # None
str = '111' # <re.Match object; span=(0, 3), match='111'>
str = ' ' # None
str = '你你' # <re.Match object; span=(0, 2), match='你你'>
str = '%%' # None
str = '@' # None
pattern = r'\w{2,3}' # 匹配单字符，至少连续两次，最多3次（字母、数字、下划线、Unicode字符（含中文））
# print(re.match(pattern, str))


# {m,} 至少m次
str = 'aa' # <re.Match object; span=(0, 2), match='aa'>
str = 'b' # None
str = '111' # <re.Match object; span=(0, 3), match='111'>
str = 'cccc' # <re.Match object; span=(0, 3), match='cccc'>
pattern = r'\w{2,}' # 匹配单字符，至少连续两次（字母、数字、下划线、Unicode字符（含中文））
print(re.match(pattern, str))
