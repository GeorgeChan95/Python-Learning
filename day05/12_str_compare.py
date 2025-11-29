#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 17:05
# @Author  : George
# @File    : 12_str_compare.py

# 运算符：>，>=，<，<=，==，!=

# 比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较
# 下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符
# 串中的后续字符将不再比较。

# 比较原理：两个字符进行比较时，比较的是其 ordinal value （原始值/码值），调用内置函
# 数 ord 可以得到指定字符的 ordinal value 。与内置函数 ord 对应的是内置函数 chr ，
# 调用内置函数 chr 时指定 ordinal value 可以得到其对应的字符。


print("tom" > "hsp")  # T
print("tom" > "to")  # T
print("tom" > "tomcat")  # F
print("tom" > "tom")  # F
print("tom" <= "tom")  # T
