#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/19 22:01
# @Author  : George
# @File    : 05_function_map_2.py

# map函数传入多个序列

def add(x, y):
    return x + y

L2 = map(add, [1, 2,3,4,5], [10, 20,30,40])
# map返回的是迭代器对象，不能直接打印， 使用 list()转换成列表方便查看
print(list(L2))  # [11, 22, 33, 44]


print("=========== 使用lamda优化 ===========")
L = map(lambda x,y: x+y, [1, 2,3,4,5], [10, 20,30,40])
# map返回的是迭代器对象，不能直接打印， 使用 list()转换成列表方便查看
print(list(L)) # [11, 22, 33, 44]