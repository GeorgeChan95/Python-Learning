#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 11:11
# @Author  : George
# @File    : 09_private_attr_method.py

# Python 私有属性和私有方法

class Clerk:
    # 公共属性
    name = None
    # 私有属性（对象不能直接访问）
    __job = None
    __salary = None

    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 公共方法
    def say(self):
        print(f"姓名：{self.name}, 工作：{self.__job}, 工资：{self.__salary}")

    # 私有方法(私有方法外部不能直接调用)
    def __get_salary(self):
        print(f"收入是：{self.__salary}")
        return self.__salary

    # 在类中定义一个公共方法，用于调用，并暴露私有方法、私有属性
    def get_salary(self):
        salary = self.__get_salary()
        return salary

c1 = Clerk('jack', '职员', 2000)
c1.say() # 可以直接调用公共方法
name = c1.name # 可以直接获取公共属性
print(f"获取到信息，姓名：{name}")

# 无法直接私有属性
# salary = c1.__salary

# 无法直接调用私有方法
# c1.__get_salary()

# 可以通过公共方法，获取到私有属性，和调用私有方法
salary = c1.get_salary()
print(f"获取到信息，工资：{salary}")

