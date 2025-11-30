#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/30 13:24
# @Author  : George
# @File    : 01_bubble_sort.py

# 冒泡排序

def bubble_sort(data_list):
    for i in range(0, len(data_list) - 1): # 外层循环控制多少论排序：列表长度减1次
        for j in range(0, len(data_list) - 1 - i): # 内层循环控制，在当前这轮循环中，要比较多少次
            if data_list[j] > data_list[j + 1]: # 如果前面的元素 > 后面的元素, 就交换
                # 这是Python的多重赋值或元组解包语法，用于同时交换两个变量的值。
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
        print(f"第{i+1}轮排序后的结果：{data_list}")

# 定义原list
data_list = [9, 2, 12,5, 7, 34, 9, 3]
# 调用冒泡排序方法
bubble_sort(data_list)
print(f"排序后，data_list内容为：{data_list}") # [2, 3, 5, 7, 9, 9, 12, 34]
