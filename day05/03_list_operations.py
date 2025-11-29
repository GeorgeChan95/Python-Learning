#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 11:09
# @Author  : George
# @File    : 03_list_operations.py

# 演示列表常用操作

list1 = [10, 20, 30]
print("list的长度：", len(list1))
print("list的最大值：", max(list1))
print("list的最小值：", min(list1))
'''
list的长度： 3
list的最大值： 30
list的最小值： 10
'''


print("############ list.append(obj),在列表末尾添加新的对象 ############")
# list.append(obj) ： 在列表末尾添加新的对象
list1.append(40)
print(list1) # [10, 20, 30, 40]


print("############ list.count(obj),统计某个元素在列表中出现的次数 ############")
print(list1.count(10)) # 1


print("############ list.extend(seq) ############")
# list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) # [10, 20, 30, 40, 1, 2, 3]


print("############ list.index(obj) ############")
# list.index(obj)： 从列表中找出某个值第一个匹配项的索引位置
# 如果找不到, 会报错: ValueError
print("30第1次出现在序列的索引是:", list1.index(30)) # 30第1次出现在序列的索引是: 2


print("############ list.reverse() ############")
list1.reverse()
print("list元素反转后：", list1) # list元素反转后： [3, 2, 1, 40, 30, 20, 10]


print("############ list.insert(index, obj) ############")
# list.insert(index, obj)：将对象插入列表指定的index位置
list1.insert(1, 80) # 索引1元素所在位置后的元素自动后移
print(list1) # [3, 80, 2, 1, 40, 30, 20, 10]