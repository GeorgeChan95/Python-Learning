#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 17:28
# @Author  : George
# @File    : 13_slice_use.py

# 切片：从一个序列中，取出一个子序列，在实际开发中，程序员经常对序列进行切片操作。
# 序列：序列是指，内容连续、有序，可使用索引的一类数据容器。

# 基本语法： 序列[起始索引:结束索引:步长]
# 表示从序列中，从指定的起始索引开始，按照指定的步长，依次取出元素，到指定结束索引为止，截取到一个新的序列。
# 切片操作是前闭后开，即 [其实索引:结束索引) ，截取的子序列包括起始索引，但是不包括结束索引。
# 步长表示，依次取出元素的间隔。
#     步长为 1：一个一个的取出元素；
#     步长为 2：每次跳过一个元素取出；
#     步长为 3，每次跳过 N-1 个元素取出。

# 切片语法: 序列[起始索引:结束索引:步长],
# (起始索引如果不写, 默认为0,
#  结束索引如果不写, 默认为截取到结尾,
#  步长如果不写, 默认为1)

# 对字符串进行切片
print("########### 对字符串进行切片 ###########")
str = "hello,world"
str_slice1 = str[0:5:1] # hello
str_slice2 = str[0:5:2] # hlo
print(str_slice1) # hello
print(str_slice2) # hlo


# 对列表进行切片
print("########### 对列表进行切片 ###########")
list_a = ["jack", "tom", "yoyo", "nono", "hsp"]
list_slice1 = list_a[1:4:1]
list_slice2 = list_a[1:4:2]
list_slice3 = list_a[0:4:3]
print(list_slice1) # ['tom', 'yoyo', 'nono']
print(list_slice2) # ['tom', 'nono']
print(list_slice3) # ['jack', 'nono']


# 对元组进行切片
print("########### 对元组进行切片 ###########")
tuple_a = (100, 200, 300, 400, 500, 600)
# 需求: 截取 (200, 300, 400, 500)

tuple_slice = tuple_a[1:5:1]
print("tuple_slice:", tuple_slice) #(200, 300, 400, 500)