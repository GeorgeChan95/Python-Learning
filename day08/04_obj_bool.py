#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/4 11:27
# @Author  : George
# @File    : 04_obj_bool.py

# bool() 是一个内置函数，用于将一个值转换为其对应的布尔值（True或False）
# 常用于判断对象是否为空

class Person:
    name = None
    age = None

p = Person()
p = None

p2 = Person()

# 通常为False的值
print("----------- 通常为False的值 -----------")
print(bool(False)) # 布尔值为False, 结果为：False
print(bool(None)) # None是False, 结果为：False
print(bool(0)) # 数值为0, 结果为：False
print(bool(0.0)) # 浮点值为0, 结果为：False
print(bool([])) # 空数组, 结果为：False
print(bool(())) # 空元组, 结果为：False
print(bool({})) # 空字典, 结果为：False
print(bool(set())) # 空集合, 结果为：False
print(bool('')) # 空字符串, 结果为：False
print(bool(p)) # 对象为None， 结果为：False


# 通常为True的值
print("----------- 通常为True的值 -----------")
print(bool(True)) # 布尔值为True, 结果为：True
print(bool(1)) # 数值不为0, 结果为：True
print(bool(-1)) # 数值不为0, 结果为：True
print(bool(0.1)) # 浮点值不为0, 结果为：True
print(bool(-0.4)) # 浮点值不为0, 结果为：True
print(bool([1, 2, 3])) # 非空数组, 结果为：True
print(bool(('张三', 1, False))) # 非空元组, 结果为：True
print(bool('李斯')) # 非空字符串, 结果为：True
print(bool({1, 1, 2, 3})) # 非空集合, 结果为：True
print(bool({'name': 'tom', 'age': 12})) # 非空字典, 结果为：True
print(bool(p2)) # 对象不为None， 结果为：True