#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 16:09
# @Author  : George
# @File    : 07_decorator_classmethod.py

# classmethod装饰器
# classmethod 这个方法是一个类方法。该方法无需实例化，没有 self 参数。
# 相对于 staticmethod 的区别在于它会接收一个指向类本身的 cls 参数。

class Person:

    def __init__(self, name):
        self.name = name

    @classmethod
    def say_hello(cls, param1):
        print(f"cls指向的类名称是：{cls.__name__}")
        print(f"执行say_hello, param1:{param1}")

if __name__ == '__main__':
    Person.say_hello('1000')

'''
打印如下：
cls指向的类名称是：Person
执行say_hello, param1:1000
'''