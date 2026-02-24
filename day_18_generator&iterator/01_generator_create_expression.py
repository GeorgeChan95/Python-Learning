#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/24 18:16
# @Author  : George
# @File    : 01_generator_create_expression.py

# 生成器的表达式方式创建

# 下面的方式创建了一个列表
L = [x * x for x in range(0, 10)]
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 将表达式创建方式中的 [] 换成 (),即可创建生成器
G = (x * x for x in range(0, 10))
print(G) # <generator object <genexpr> at 0x0000029F7697F850>
print(G.__next__()) # 0
print(G.__next__()) # 1
print(G.__next__()) # 4