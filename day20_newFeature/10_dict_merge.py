#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 20:08
# @Author  : George
# @File    : 10_dict_merge.py

dict1 = {'a':1}
dict2 = {'b':2}
#旧版本
dict1.update(dict2)
print(dict1) # {'a': 1, 'b': 2}

#新版本 |
result = dict1 | dict2
print(result) # {'a': 1, 'b': 2}

#更新字典
dict1 |= dict2  #等价于 dict1 = dict1 | dict2
print(dict1) # {'a': 1, 'b': 2}
