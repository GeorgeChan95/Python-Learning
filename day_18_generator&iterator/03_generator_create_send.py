#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/24 18:50
# @Author  : George
# @File    : 03_generator_create_send.py

# 生成器 send 方法的使用

# send的作用是唤醒并继续执行，发送一个信息到生成器内部
def foo():
    print("start")
    i = 0
    while i < 3:
        temp = yield i
        print(f"temp:{temp}")
        i = i + 1
    print("end")


g = foo() # 实例化方法，创建生成器，此时函数没有执行，不打印任何东西
print(next(g))  # 相当于g.__next__()，yield 做了两件事：1、把 0 返回给 next(g)  2、暂停在这一行，到这里打印了 start 和 0
print("********") # 打印 ********
print(g.send(100)) # 等价于 temp = 100， 然后继续往下执行。打印 temp:100，然后 i + 1,进入下一轮 while 循环，且停在 yield i，此时 yield 1，所以打印：1
print(next(g)) # 这里temp是None，yield 2， 因此打印 temp:None， 2

# 可以通过 for 循环，遍历 生成器
for a in g:
    print("in ", a)
