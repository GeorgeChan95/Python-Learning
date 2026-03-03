#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/3 13:52
# @Author  : George
# @File    : 10_group_match.py

# 分组匹配

# 如果一个模式字符串中有用一对圆括号括起来的部分，那么这部分就会作为一组，可以通过group方法的参数获取指定的组匹配的字
# 符串。当然，如果模式字符串中没有任何用圆括号括起来的部分，那么就不会对待匹配的字符串进行分组。

import re

r'''
(ab) 将括号中的字符作为一个分组
\num 引用分组num匹配到的字符串
(?P<name>) 分别起组名
(?P=name) 引用别名为name分组匹配到的字符串
'''

# 匹配座机号码（不使用分组）
# 区号{3,4}-电话号码{5,8}
pattern = r'\d{3,4}-[1-9]\d{4,7}$'
str = '010-1234567' # <re.Match object; span=(0, 11), match='010-1234567'>
str = '0551-66823711' # <re.Match object; span=(0, 13), match='0551-66823711'>
# print(re.match(pattern, str))


# 匹配座机号码（使用分组）
# 区号{3,4}-电话号码{5,8}
pattern = r'(\d{3,4})-([1-9]\d{4,7}$)'
str = '010-1234567' # <re.Match object; span=(0, 11), match='010-1234567'>
str = '0551-66823711' # <re.Match object; span=(0, 13), match='0551-66823711'>
s = re.match(pattern, str)
print(s) # <re.Match object; span=(0, 13), match='0551-66823711'>
print(s.group(0)) # 0551-66823711
print(s.group(1)) # 0551
print(s.group(2)) # 66823711
# 下面是打印的匹配内容：电话号码
print(s.group()[0]) # 0
print(s.group()[1]) # 5
print(s.group()[2]) # 5
print(s.group()[3]) # 1



################ \num的使用 ################
# .+ 为贪婪匹配，不使用分组 \num ,无法正确匹配网页结构
print("################ \\num的使用 ################")
s = '<html><head>分组的使用</head></html>' # 正确的格式
s1 = '<html><head>分组的使用</body></h1>' # 错误的格式
pattern = r'<.+><.+>.+</.+></.+>' # 等效于：<任意内容><任意内容>任意内容</任意内容></任意内容>
print(re.match(pattern, s)) # <re.Match object; span=(0, 31), match='<html><head>分组的使用</head></html>'>
print(re.match(pattern, s1)) # 错误的格式依然可以匹配 <re.Match object; span=(0, 29), match='<html><head>分组的使用</body></h1>'>

# 使用 \num
# #优化后 可以使用分组 \2 表示引用第2个分组 \1表示引用第1个分组
pattern = r'<(.+)><(.+)>.+</\2></\1>'
print(re.match(pattern, s)) # 匹配正确的网页结构：<re.Match object; span=(0, 31), match='<html><head>分组的使用</head></html>'>
print(re.match(pattern, s1)) # 错误的网页结构不匹配：None


################  ################
# 如果分组比较多的话，数起来比较麻烦，可以使用起别名的方法?P<要起的名字> 以及使用别名(?P=之前起的别名)
print("################ 分组起别名 ################")
s = '<html><head>分组的使用</head></html>'
pattern = r'<(?P<Key1>.+)><(?P<Key2>.+)>.+</(?P=Key2)></(?P=Key1)>'
print(re.match(pattern, s)) # <re.Match object; span=(0, 31), match='<html><head>分组的使用</head></html>'>