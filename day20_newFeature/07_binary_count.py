#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 19:46
# @Author  : George
# @File    : 07_binary_count.py

# 二进制数中1的个数

num = 4
#旧版本
print(bin(num)) # 0b100
print('出现1的次数：',bin(num).count('1')) # 出现1的次数： 1

#新版本 bit_count()
print('出现1的次数：',num.bit_count()) # 出现1的次数： 1