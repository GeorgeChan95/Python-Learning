#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/12 15:12
# @Author  : George
# @File    : 03_exceptions_exercise.py

age = 0
while True:
    try:
        age = int(input("请输入年龄，要求是整数："))
        break
    except Exception as e:
        print("你输入的年龄不是整数，请重新输入")

print(f"你输入的年龄是：{age}")