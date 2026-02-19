#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/19 22:15
# @Author  : George
# @File    : 06_function_reduce.py
from functools import reduce


# reduce函数：reduce() 是 Python 里用于把一个序列“归并/累积”成一个结果的函数。
# 它会不断地把前两个元素计算出一个结果，再拿这个结果和下一个元素继续计算，直到最后只剩一个值。

def f(x, y):
    '''
    定义函数，对传入的参数做加法运算
    :param x:
    :param y:
    :return:
    '''
    return x + y


# 使用 reduce 函数，对集合中的每一个元素，都执行f函数，计算出结果
num1 = reduce(f, [1, 2, 3, 4, 5])
print(num1) # 15

print("======= 使用lamda优化 =======")
num2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(num2) # 15
