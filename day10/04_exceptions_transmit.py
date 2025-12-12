#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/12 15:21
# @Author  : George
# @File    : 04_exceptions_transmit.py

def f3():
    print("---f3() start----")
    try:
        print(10 / 0)
    except Exception as e:
        print(f"f3()捕获了异常，hi {e}")
    print("---f3() end----")

def f2():
    print("---f2() start---")
    f3()
    print("---f2() end---")

def f1():
    try:
        f2()
    except Exception as e:
        print(f"f1()捕获异常->{e}")

f1()