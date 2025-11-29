#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 18:04
# @Author  : George
# @File    : 17_set_create.py

set_a = {ele for ele in range(1, 6)}
print(set_a) # {1, 2, 3, 4, 5}


set_b = {ele for ele in 'abc'}
print(set_b) # {'b', 'c', 'a'}