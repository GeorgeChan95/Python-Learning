#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 19:11
# @Author  : George
# @File    : 04_func_type_hint.py

# 函数参数和返回类型标注

#定义一个函数
#参数 num int类型
#返回值 字符串类型
def sum(num: int) -> str:
    return f'num值是：{num}'

print(sum(60)) # num值是：60



#定义函数 两个参数都是int 返回int
def sum_fun(a:int,b:int)->int:
    return a+b



#定义函数参数添加默认值
# 当函数 sum3_fun b参数为空是，设置默认值 3.1
def sum3_fun(a:int, b:float=3.14) -> float:
    return a + b
print(sum3_fun(10)) # 13.14
print(sum3_fun(20, 45.1)) # 65.1




# 定义变量 指向一个函数
# Callable用于标注可调用对象（函数、方法等）的类型
from typing import Callable
# 变量newF 指向函数 sum3_fun
# [[int, float], float] 表示 sum3_fun 的入参类型和返回值类型
newF:Callable[[int, float], float] = sum3_fun
# 调用变量函数
print(newF(10, 2.3)) # 12.3




#定义函数，产生整数的生成器，每次返回一个
from typing import Iterator
def return_fun(num: int) -> Iterator[int]:
    i = 0
    while i < num:
        yield i
        i += 1

# 生成器是一个特殊的迭代器
print(return_fun(3)) # <generator object return_fun at 0x000001EA50226D40>
for i in return_fun(3):
    print(i)
'''
0
1
2
'''
