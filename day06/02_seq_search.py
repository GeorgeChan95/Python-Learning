#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/30 13:43
# @Author  : George
# @File    : 02_seq_search.py

# 顺序查找

def seq_search_one(data_list, find_val):
    '''
    从数据集中查找元素第一次出现的下标位置
    :param data_list: 原数据集
    :param find_val: 要查找的元素
    :return:
    '''
    find_index = -1
    for i in range(0, len(data_list)):
        if(data_list[i] == find_val):
            find_index = i

    if (find_index == -1):
        print(f"没有从集合中找到元素：{find_val}")
    else:
        print(f"从集合data_list中找到元素：{find_val}, 下标为：{find_index}")

    # 将元素在集合中第一次出现的下标返回
    return find_index

data_list = [10, 20, 30, 40, 50, 60]
find_val = 30

index1 = seq_search_one(data_list, find_val)
index2 = seq_search_one(data_list, 80)
print(f"元素{find_val}下标为：", index1) # 元素30下标为： 2



def seq_search_all(data_list, find_val):
    '''
    从数据集中查找元素出现的所有下标位置
    :param data_list: 原数据集
    :param find_val: 要查找的元素
    :return:
    '''
    find_index = []
    for i in range(0, len(data_list)):
        if(data_list[i] == find_val):
            find_index.append(i)

    if (len(find_index) <= 0):
        print(f"没有从集合中找到元素：{find_val}")
    else:
        print(f"从集合data_list中找到元素：{find_val}, 下标为：{find_index}")

    # 将元素在集合中第一次出现的下标返回
    return find_index

data_list2 = [10, 20, 30, 40, 50, 60, 30, 40, 20]
find_val = 30

index_list = seq_search_all(data_list2, find_val)
print(f"元素{find_val}, 在集合中的下标位置为：{index_list}") # 元素30, 在集合中的下标位置为：[2, 6]