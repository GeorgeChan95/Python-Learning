#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 16:13
# @Author  : George
# @File    : 08_decorator_class.py

# 类装饰器
# 类能实现装饰器的功能， 是由于当我们调用一个对象时，实际上调
# 用的是它的 __call__ 方法。

class Demo:
    def __call__(self, *args, **kwargs):
        print("执行了call方法")

if __name__ == '__main__':
    d1 = Demo()
    d1() # 直接调用实例化对象，打印：执行了call方法

class myLogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("日志记录")
        # 执行传入的函数
        self.func(*args, **kwargs)

@myLogDecorator
def my_fun(a, b):
    print("执行函数....")

if __name__ == '__main__':
    my_fun(1, 2)
'''
运行打印如下：
日志记录
执行函数....
'''