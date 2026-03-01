#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/1 10:58
# @Author  : George
# @File    : 02_match_flag.py

# 正则表达式match函数，flag的使用
# re.I 使匹配对大小写不敏感
# re.L 做本地化识别（locale-aware）匹配
# re.M 多行匹配，影响 ^ 和 $
# re.S 使 . 匹配包括换行在内的所有字符
# re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B
# re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

import re

s = 'hello python'
pattern = 'Hello' # 正则表达式与匹配的字符串大小写不同
# 定义正则表达式，设置 flag 标识为：忽略大小写
result = re.match(pattern, s, re.I)
if result is not None:
    print("匹配成功，结果是:", result.group())
else:
    print("匹配失败")