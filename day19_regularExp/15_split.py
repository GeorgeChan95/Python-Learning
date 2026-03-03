#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/3 18:23
# @Author  : George
# @File    : 15_split.py

# split函数
# split函数用于根据正则表达式分隔字符串，也就是说，将字符串与
# 模式匹配的子字符串都作为分隔符来分隔这个字符串。split函数返
# 回一个列表形式的分隔结果，每一个列表元素都是分隔的子字符
# 串。语法格式如下：
# re.split(pattern, string[, maxsplit=0,flags=0])

'''
pattern 匹配的正则表达式
string 要匹配的字符串。
maxsplit 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''

import  re

s = 'a 1 b 2 c 3 d'
pattern = r'\d+'
result = re.split(pattern,s)
print(result) # ['a ', ' b ', ' c ', ' d']

#指定分隔的次数
print(re.split(pattern,s,maxsplit=2)) # ['a ', ' b ', ' c 3 d']