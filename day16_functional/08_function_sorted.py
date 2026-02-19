#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/19 22:27
# @Author  : George
# @File    : 08_function_sorted.py

# sorted 函数实现元素的排序

# int 默认以升序排序
sorted1 = sorted([0, -1, 2, 7, -2])
print(list(sorted1)) # [-2, -1, 0, 2, 7]

# 字符串默认以 ASCII 码排序
sorted2 = sorted(['A', 'a', 'B', 'b', 'C', 'c'])
print(list(sorted2)) # ['A', 'B', 'C', 'a', 'b', 'c']

# 指定key函数，实现自定义排序，这里指定以绝对值大小升序排序
sorted3 = sorted([0, -1, 2, 7, -2], key=abs)
print(list(sorted3)) # [0, -1, 2, -2, 7]

# 忽略大小写排序
sorted4 = sorted(['A', 'a', 'B', 'b', 'C', 'c'], key=str.lower)
print(list(sorted4)) # ['A', 'a', 'B', 'b', 'C', 'c']

# 排序反转
sorted5 = sorted([0, -1, 2, 7, -2], reverse=True)
print(list(sorted5)) # [7, 2, 0, -1, -2]


