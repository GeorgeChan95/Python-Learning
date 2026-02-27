#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/27 19:01
# @Author  : George
# @File    : 09_slot.py

# slot 可以限制动态添加成员变量和成员方法，但是不能限制动态添加类的方法和属性

class Person:
    __slots__ = ("name", "age")
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p1 = Person("张三", 18)
    # p1.score = 80 # 报错，因为 score 不在 __slots__ 中, AttributeError: 'Person' object has no attribute 'score'
    # print(p1.score)

    Person.gender = "男" # 动态添加类的属性是不受限制的
    print(p1.gender)
