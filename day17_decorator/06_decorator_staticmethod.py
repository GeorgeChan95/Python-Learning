#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 16:04
# @Author  : George
# @File    : 06_decorator_staticmethod.py

# 内置装饰器，staticmethod
# staticmethod 装饰器同样是用于类中的方法，这表示这个方法将会是一
# 个静态方法，意味着该方法可以直接被调用无需实例化，但同样意
# 味着它没有 self 参数，也无法访问实例化后的对象。

class Person:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def say_hello(param1):
        print(f"执行say_hello, param1:{param1}")

if __name__ == '__main__':
    Person.say_hello('1000')

'''
打印如下：
执行say_hello, param1:1000
'''