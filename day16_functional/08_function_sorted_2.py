#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/19 22:34
# @Author  : George
# @File    : 08_function_sorted_2.py
from functools import cmp_to_key


# sorted 实现类的自定义排序

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = Student('Tom', 10)
stu2 = Student('Jerry', 20)
stu3 = Student('Ketty', 30)


def custom_sorted(stu1, stu2):
    if stu1.age > stu2.age:
        return 1
    elif stu1.age < stu2.age:
        return -1
    else:
        return 0

s_list = sorted([stu1, stu2, stu3], key=cmp_to_key(custom_sorted))
for stu in s_list:
    print(f"name:{stu.name} === age:{stu.age}")
'''
name:Tom === age:10
name:Jerry === age:20
name:Ketty === age:30
'''

print("====== lamda优化 ======")
s2_list = sorted([stu1, stu2, stu3], key=lambda x:x.age, reverse=True)
for stu in s2_list:
    print(f"name:{stu.name} === age:{stu.age}")
'''
name:Ketty === age:30
name:Jerry === age:20
name:Tom === age:10
'''