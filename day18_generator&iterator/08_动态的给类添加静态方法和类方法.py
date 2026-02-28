#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/27 18:29
# @Author  : George
# @File    : 08_动态的给类添加静态方法和类方法.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 定义在class之外的静态方法
@staticmethod
def say():
    print("我是一个人")

# 定义在class之外的类方法,必须添加参数cls,因为类方法是作用于类的,而不是对象的
@classmethod
def run(cls):
    print("我会跑步")

if __name__ == '__main__':

    print("========= 静态方法")
    # 通过Class.方法名的方式，将say方法添加到Person类中
    Person.say = say

    # 通过类名.方法名的方式调用say方法
    Person.say()
    Person.score = 100
    print("p1的成绩是：", Person.score)

    # 通过Class.方法名的方式，将run方法添加到Person类中
    Person.run = run
    # 通过类名.方法名的方式调用run方法
    Person.run()
