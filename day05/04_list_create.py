#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 13:37
# @Author  : George
# @File    : 04_list_create.py

# 创建List数据集

# 方式1
list1 = [ele * 2 for ele in range(1, 5)] # range(1, 5) 生成集合 [1, 2, 3, 4]
print(list1) # [2, 4, 6, 8]

list2 = [ele + ele for ele in "abc"] # for ele in "abc" 会遍历字符串中的每个字符
print(list2) # ['aa', 'bb', 'cc']