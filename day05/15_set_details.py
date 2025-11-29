#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 17:41
# @Author  : George
# @File    : 15_set_details.py

# set 的特点

# 1、集合是由不重复元素组成的无序容器
print("########### set自动去重 ###########")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket内容为：", basket) # basket内容为： {'pear', 'banana', 'orange', 'apple'}


# 无序, 也就是你定义元素的顺序和取出的顺序不能保证一致,
# 集合底层会按照自己的一套算法来存储和取数据, 所以每次取出顺序是不变的
print("########### set是无序的 ###########")
set_a = {100, 200, 300, 400, 500}
print(f"set_a: {set_a}") # set_a: {400, 100, 500, 200, 300}
print(f"set_a: {set_a}") # set_a: {400, 100, 500, 200, 300}
print(f"set_a: {set_a}") # set_a: {400, 100, 500, 200, 300}
print(f"set_a: {set_a}") # set_a: {400, 100, 500, 200, 300}



# 集合不支持索引 ,会报错
print("########### set不支持索引 ###########")
# print(set_a[0])
r'''
Traceback (most recent call last):
  File "E:\study\PythonLearning\Python-Learning\day05\15_set_operations.py", line 28, in <module>
    print(set_a[0])
          ~~~~~^^^
TypeError: 'set' object is not subscriptable
'''


# 使用for对集合进行遍历
print("########### 使用for对集合进行遍历 ###########")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for ele in basket:
    print(ele)


# 创建空集合只能用 set()，不能用 {}，{} 创建的是空字典
print("########### set创建空集合 ###########")
set_b = {}  # 上面这样定义空集合不对，他是一个空字典
set_c = set()  # 创建空集合
print(f"set_b: {set_b} 类型: {type(set_b)}  set_c: {set_c} 类型: {type(set_c)}") # set_b: {} 类型: <class 'dict'>  set_c: set() 类型: <class 'set'>