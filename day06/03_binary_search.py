#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/30 13:56
# @Author  : George
# @File    : 03_binary_search.py


def binary_search(data_list, find_val):
    r'''
    二分查找
    :param data_list:
    :param find_val:
    :return:
    '''
    left_index = 0  # 左索引
    right_index = len(data_list) - 1  # 右索引
    find_index = -1
    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        if data_list[mid_index] > find_val:
            right_index = mid_index -1
        elif data_list[mid_index] < find_val:
            left_index = mid_index + 1
        elif data_list[mid_index] == find_val:
            find_index = mid_index
            left_index = mid_index + 1
            right_index = mid_index - 1
        else:
            break

    return find_index


data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
find_val = 6
find_val2 = 30
index1 = binary_search(data_list, find_val)
# index2 = binary_search(data_list, find_val2)

print(f"{find_val} 在集合中的位置：{index1}")
# print(f"{find_val2} 在集合中的位置：{index2}")