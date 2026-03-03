#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/3 18:16
# @Author  : George
# @File    : 11_sub_subn.py

import re

# sub() 和 subn() 搜索与替换
# sub函数和subn函数用于实现搜索和替换功能。这两个函数的功能
# 几乎完全相同，都是将某个字符串中所有匹配正则表达式的部分替
# 换成其他字符串。用来替换的部分可能是一个字符串，也可以是一
# 个函数，该函数返回一个用来替换的字符串。sub函数返回替换后
# 的结果，subn函数返回一个元组，元组的第1个元素是替换后的结
# 果，第2个元素是替换的总数。语法格式如下：
# re.sub(pattern, repl, string, count=0,flags=0)

phone = "2004-959-559 # 这是一个国外电话号码"
# 替换目标字符串中注释
pattern = r'#.*$'
print(re.sub(pattern, "", phone)) # 2004-959-559
# 删除非数字(-)的字符串
pattern = r'\D'
print(re.sub(pattern, "", phone)) # 2004959559

# 使用 subn()
result = re.subn(pattern, "", phone)
print(result) # ('2004959559', 15)
print("替换结果：", result[0]) # 替换结果： 2004959559
print("替换次数：", result[1]) # 替换次数： 15