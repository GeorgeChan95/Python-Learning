#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/1 10:43
# @Author  : George
# @File    : 01_match_test.py

# 正则表达式match的使用
# re.match是用来进行正则匹配检查的方法，如果字符串开头的0个或多个字符匹配正则表达式
# 模式，则返回相应的match对象。如果字符串不匹配模式，返回None（注意不是空字符串""）

# 匹配对象Match Object具有group()方法， 用来返回字符串的匹配部分,具有span()方法。返回
# 匹配字符串的位置（元组存储开始，结束位置），具有start(),end()方法，存储匹配数据的开
# 始和结束位置。（也可以通过对象的dir(对象查看对象的方法)）

import re

# 匹配字符串开头的hello
pattern = "hello"
# 待匹配的字符串
str = "hello world"
# 测试match函数
result = re.match(pattern, str)
print(result) # <re.Match object; span=(0, 5), match='hello'>
print(result.span()) # (0, 5)
print(result.group()) # hello
print(result.start()) # 0
print(result.end()) # 5
