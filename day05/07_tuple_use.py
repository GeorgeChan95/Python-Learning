#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 14:54
# @Author  : George
# @File    : 07_tuple_use.py

# tuple 的使用
print("########### tuple 的使用 ###########")
tuple1 = ('a', 'b', 'c', 'd', 'e')
print("第3个元素：", tuple1[2]) # 第3个元素： c


print("########### tuple使用while循环 ###########")
tuple2 = tuple(ele for ele in range(1, 7))
print(tuple2)      # 输出：(1, 2, 3, 4, 5, 6)
# print(tuple2[0])   # 输出：1
index = 0
while index < len(tuple2):
    print(tuple2[index])
    index += 1

print("########### tuple使用for循环 ###########")
tuple3 = ('red', 'green', 'blue', 'yellow', 'white', 'black')
for ele in tuple3:
    print(ele)
