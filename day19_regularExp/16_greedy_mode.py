#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/3 18:41
# @Author  : George
# @File    : 16_greedy_mode.py

import re

# 贪婪模式和非贪婪模式
# 贪婪模式指Python里数量词默认是贪婪的，总是尝试匹配尽可能多
# 的字符。非贪婪模式与贪婪相反，总是尝试匹配尽可能少的字符，
# 可以使用"*"，"?"，"+"，"{m,n}"后面加上？，使贪婪变成非贪婪。

# 贪婪模式
s = 'This is my tel:133-1234-1234'
pattern = r'(.+)(\d+-\d+-\d+)'
result = re.match(pattern,s)
# print(result.group()) # This is my tel:133-1234-1234
# print(result.group(1)) # This is my tel:13
# print(result.group(2)) # 3-1234-1234


# 修改为非贪婪模式
# ? 让匹配变成非贪婪模式：只要后面还能匹配成功，我就少吃一点
s = 'This is my tel:133-1234-1234'
pattern = r'(.+?)(\d+-\d+-\d+)'
result = re.match(pattern,s)
# print(result.group()) # This is my tel:133-1234-1234
# print('第一个分组匹配结果：',result.group(1)) # 第一个分组匹配结果： This is my tel:
# print('第二个分组匹配结果：',result.group(2)) # 第二个分组匹配结果： 133-1234-1234


s = 'abc123'
pattern = r'abc(\d+)'
result = re.match(pattern,s)
# print(result.group(1))  #贪婪模式 匹配结果 123


pattern = r'abc(\d+?)'
result = re.match(pattern,s)
print(result.group(1)) # 1, 非贪婪模式，匹配一个即停止
print(result.group()) # abc1
