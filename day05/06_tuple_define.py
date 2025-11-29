#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 14:10
# @Author  : George
# @File    : 06_tuple_define.py

# typle 的定义

tuple1 = (1, 'a', 3)
print(f"元组的内容: {tuple1}, 类型：{type(tuple1)}") # 元组的内容: (1, 'a', 3), 类型：<class 'tuple'>

# 定义空的 tuple
# 方式1
tuple2 = tuple()
# 方式2
tuple3 = ()
print("tuple2:", tuple2)
print("tuple3:", tuple3)