#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/12 15:50
# @Author  : George
# @File    : 05_customize_exception.py

class AgeException(Exception):
    pass

while True:
    try:
        age = int(input("请输入年龄（18-120）："))
        if not (age >= 18 and age <= 120):
            raise AgeException("年龄需要在18-120之间")
        break
    except ValueError as e:
        print("输入的不是整数")
        print(e)

