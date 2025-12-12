#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/12 11:25
# @Author  : George
# @File    : 01_exception_01.py

res = None
try:
    num1 = 10
    num2 = 0
    res = num1 / num2
    # res = num2 / num1
except Exception as e:
    print(f"捕获到异常信息：{e}，异常类型：{type(e)}")
else:
    print(f"没有发生异常，计算结果：{res}")
finally:
    print(f"计算完成，结果为：{res}")