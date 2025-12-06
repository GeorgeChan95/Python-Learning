#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 9:53
# @Author  : George
# @File    : 06_self_class_exercise.py

# ● 定义Person类
# 1) 里面有name、age属性
# 2) 并提供compare_to比较方法，用于判断是否和另一个人相等
# 3) 名字和年龄都一样，就返回True, 否则返回False

class Person:
    name = None
    age = None

    def compare_to(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

p1 = Person()
p1.name = 'jack'
p1.age = 18

p2 = Person()
p2.name = 'tim'
p2.age = 18

print(f"p1是否等于p2: {p1.compare_to(p2)}") # p1是否等于p2: False