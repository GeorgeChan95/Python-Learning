#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 19:51
# @Author  : George
# @File    : 08_dict.py

# 字典新特性
data = {'a':1,'b':2,'c':3}
print(data.items())
print(data.keys())
print(data.values())


# 使用keys()遍历
for key in data.keys():
    print(f"键: {key}, 值: {data[key]}")


if 'b' in data.keys():
    print("键 'b' 存在")

# 更简洁的写法（直接检查字典也可以）
if 'b' in data:
    print("键 'b' 存在")


# 转换为列表
keys_list = list(data.keys())
print(keys_list)  # ['a', 'b', 'c']



################## 新特性 ##################
#新特性
keys = data.keys()
items = data.items()
values = data.values()
print('mapping:',keys.mapping)
print('mapping:',items.mapping)
print('mapping:',values.mapping)

for key in keys.mapping:
    print(f"键1: {key}, 值1: {data[key]}")


#旧版本
keys = ['name','age','sex']
values = ['zs',23,'man', 'male']
data_dict = dict(zip(keys,values)) # 只取前3个键值对
print('创建的字典对象：',data_dict) # 创建的字典对象： {'name': 'zs', 'age': 23, 'sex': 'man'}

data_dict2 = dict(zip(keys, values, strict=True)) # 严格模式，键值对数量必须匹配
print('创建的字典对象2：',data_dict2)
'''
Traceback (most recent call last):
  File "E:\study\PythonLearning\Python-Learning\day20_newFeature\08_dict.py", line 53, in <module>
    data_dict2 = dict(zip(keys, values, strict=True))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: zip() argument 2 is longer than argument 1
'''
