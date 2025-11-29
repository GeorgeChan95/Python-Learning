#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 16:50
# @Author  : George
# @File    : 11_chr_ord.py

# ord()：对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。例如 ord('a') 返回整数 97
# chr()：返回 Unicode 码位为整数 i 的字符的字符串格式。例如， chr(97) 返回字符串 'a'

print(ord('1')) # 49
print(ord('2')) # 50
print(ord('a')) # 97
print(ord('b')) # 98


print("-------------------")
print(chr(49))  # 1
print(chr(97))  # a