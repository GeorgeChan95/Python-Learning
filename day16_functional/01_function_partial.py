#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/11 9:56
# @Author  : George
# @File    : 01_function_partial.py
from functools import partial

# 偏函数

# 1、定义偏函数
int3 = partial(int, base=2)
# 2、使用偏函数
print(int3('10')) # 2
print(int3('1010')) # 10


# 不使用偏函数
int2 = int('1010', base=2)
print(int2) # 10


