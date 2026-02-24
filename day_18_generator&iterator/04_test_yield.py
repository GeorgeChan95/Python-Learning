#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/24 19:07
# @Author  : George
# @File    : 04_test_yield.py

# 测试 yield 的使用

def test():
    i = 0
    while i < 10:
        yield i
        i += 1
    return -1

a = test()
print(a.__next__()) # 0 第一次执行，yield 0，返回 0
print(a.__next__()) # 1 第二次执行，yield 1，返回 1
print(a.__next__()) # 2 第三次执行，yield 2，返回 2
print(a.__next__()) # 3 第四次执行，yield 0，返回 3