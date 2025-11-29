#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 15:30
# @Author  : George
# @File    : 09_tuple_operations.py

# tuple 常用操作
print("########### len()、max()、min() ###########")
tuple_a = (100, 200, 300, 400, 600, 200)
print("tuple_a的元素数量：", len(tuple_a)) # tuple_a的元素数量： 6
print("tuple_a的最大值：", max(tuple_a)) # tuple_a的最大值： 600
print("tuple_a的最小值：", min(tuple_a)) # tuple_a的最小值： 100


# tuple.count(obj) ： 统计某个元素在列表中出现的次数
print("########### tuple.count(obj) ###########")
tuple_b = (100, 200, 300, 400, 600, 200)
print("tuple_b中100出现的次数", tuple_b.count(100)) # tuple_b中100出现的次数 1
print("tuple_b中200出现的次数", tuple_b.count(200)) # tuple_b中200出现的次数 2



# tuple.index(obj)： 从列表中找出某个值第一个匹配项的索引位置
print("########### tuple.index(obj) ###########")
tuple_c = (100, 200, 300, 400, 600, 200)
print("tuple_c中元素200第一次出现的索引位置：", tuple_c.index(200)) # tuple_c中元素200第一次出现的索引位置： 1


# 判断是否包含某个元素
print("########### 判断是否包含某个元素 ###########")
tuple_d = (100, 200, 300, 400, 600, 200)
flag1 = 3000 in tuple_d
flag2 = 200 in tuple_d
print("tuple_d中是否包含元素3000：", flag1) # tuple_d中是否包含元素3000： False
print("tuple_d中是否包含元素200：", flag2) # tuple_d中是否包含元素200： True
