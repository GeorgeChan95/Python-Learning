#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 17:38
# @Author  : George
# @File    : 14_set_define.py

# Set 的定义

set_a = {100, 200, 300, 400}
print(set_a) # {200, 100, 400, 300}


# 空集合只能用 set()
set_b = set()
print(f"set_b:{set_b}, 类型是：{type(set_b)}") # set_b:set(), 类型是：<class 'set'>