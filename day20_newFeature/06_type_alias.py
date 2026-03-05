#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 19:38
# @Author  : George
# @File    : 06_type_alias.py

# 类型别名的更改


# 旧版本
'''
将Python内置的str类型赋值给变量oldStr
这创建了一个类型别名，oldStr现在指向str类型
相当于给str起了一个别名
'''
oldStr = str
msg: oldStr = "Hello, World!"
print(f"{msg:}")


# 新版本
from typing import TypeAlias

newStr: TypeAlias = str
newInt: TypeAlias = int
def num_fun(num: newInt | newStr) -> newInt | newStr:
    return num + 100
print(num_fun(10)) # 110


