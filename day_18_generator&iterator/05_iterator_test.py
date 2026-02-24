#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/24 19:19
# @Author  : George
# @File    : 05_iterator_test.py

from collections.abc import Iterator
from collections.abc import Iterable

# 列表、字典、字符串都是可迭代对象，但不是迭代器

print(type([])) # <class 'list'>
a = isinstance([], Iterator)
print(a) # False列表不是迭代器

b = isinstance([], Iterable)
print(b) # True 列表对象可迭代

print(type({})) # <class 'dict'>
c = isinstance({}, Iterator)
print(c) # False

print(type("")) # <class 'str'>
print(isinstance("", Iterator)) # False

# 将列表、字典、字符串转换成迭代器, 使用 iter() 方法
print("***********************")
print(isinstance(iter([]), Iterator)) # True
print(isinstance(iter("123"), Iterator)) # True
print(isinstance(iter({'name': 'George'}), Iterator)) # True