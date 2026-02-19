#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/19 22:23
# @Author  : George
# @File    : 07_function_filter.py

# Python filter 函数实现元素过滤功能

# 判断传入的元素是否为偶数
def is_odd(x):
    return x % 2 == 0


# 使用 filter 函数，将满足is_odd 判断条件的元素放入新的集合中返回
list1 = filter(is_odd, [0, 1, 2, 3, 4, 5, 6])
print(list(list1))  # [0, 2, 4, 6]

print("====== 使用lamda ======")

list2 = filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4, 5, 6])
print(list(list2))  # [0, 2, 4, 6]
