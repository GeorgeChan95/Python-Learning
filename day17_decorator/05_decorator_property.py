#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 15:54
# @Author  : George
# @File    : 05_decorator_property.py

# 内置装饰器 property
# property 装饰器用于类中的函数，使得我们可以像访问属性一样来获取一个函数的返回值。

class User:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property # 使用内置装饰器 property，可以方便的访问函数的返回结果
    def totalSalary(self):
        return int(self.salary) * 12

    # 不使用 @property
    def totalSalary2(self):
        return int(self.salary) * 12

if __name__ == '__main__':
    u1 = User('tom', 3000)
    total = u1.totalSalary2()
    # 由于使用了 @property 装饰器，这里可以像使用属性一样，获取函数的返回结果
    print(f"{u1.name} 年薪为：{u1.totalSalary}, 调用方法返回：{total}")