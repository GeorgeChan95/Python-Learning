#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 19:32
# @Author  : George
# @File    : 05_mixed_type.py

# 旧版本
from typing import Union
def num_fun(num:Union[int, float]) -> Union[int, float]:
    return num + 10
print(num_fun(10)) # 20
print(num_fun(10.2)) # 20.2


# 新版本
def num2_fun(num: int | float) -> int | float:
    return num + 100
print(num2_fun(20)) # 120
print(num2_fun(20.5)) # 120.5