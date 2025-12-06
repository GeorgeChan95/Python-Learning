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


class Student:
    def __init__(self, name, age):
        print("可以通过构造器，动态的给对象生成属性")
        self.name = name
        self.age = age

s1 = Student("tim", 20)

print(f"学生姓名：{s1.name}, 年龄：{s1.age}") # 学生姓名：tim, 年龄：20