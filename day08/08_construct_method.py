#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 10:37
# @Author  : George
# @File    : 08_construct_method.py

class Person:
    name = None
    age = None

    def __init__(self):
        print("对象在创建时，自动执行构造方法")

    def __init__(self, name, age):
        print("一个类，最多只能有一个构造方法，如果有多个，那么最后一个构造方法能够生效")
        self.name = name
        self.age = age

p1 = Person("Tom", 30)
