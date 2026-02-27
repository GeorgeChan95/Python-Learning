#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/27 18:19
# @Author  : George
# @File    : 07_动态给对象添加属性和方法.py
import types


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p1 = Person("张三", 18)
    print(p1.name)
    print(p1.age)

    # 动态的给对象添加score属性
    p1.score = 80
    print("p1的成绩是：", p1.score)

    def say(self):
        print("我是", self.name, "我今年", self.age, "岁")

    # 动态的给对象添加方法
    p1.say = types.MethodType(say, p1)

    p1.say()

'''
张三
18
p1的成绩是： 80
我是 张三 我今年 18 岁
'''