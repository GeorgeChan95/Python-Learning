#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/30 11:12
# @Author  : George
# @File    : 20_dict_operations.py

# 字典的常用操作

# 定义字典
dict_a = {"one": 1, "two": 2, "three": 3}

# 1  len(d): 返回字典 d 中的项数
print("########### len(d) ###########")
print(f"字典dict_a中的项数：{len(dict_a)}") # 字典dict_a中的项数：3


# 2  d[key]: 返回 d 中以 key 为键的项。 如果映射中不存在 key 则会引发 KeyError
print("########### d[key] ###########")
print(dict_a["three"]) # 3
# print(dict_a["four"]) # KeyError: 'four'
r'''
Traceback (most recent call last):
  File "E:\study\PythonLearning\Python-Learning\day05\20_dict_operations.py", line 20, in <module>
    print(dict_a["four"]) # 3
          ~~~~~~^^^^^^^^
KeyError: 'four'
'''


# 3  d[key] = value: 将 d[key] 设为 value, 如果key已经存在，则是修改value,
# 如果key没有存在，则是增加 key-value, 注意会直接修改原来的字典
print("########### 修改字典 ###########")
dict_a["one"] = 'a'
dict_a["four"] = 4
print(f"字典项数：{len(dict_a)}, 内容：{dict_a}") # 字典项数：4, 内容：{'one': 'a', 'two': 2, 'three': 3, 'four': 4}


# 4  del d[key]: 将 d[key] 从 d 中移除。 如果映射中不存在 key 则会引发 KeyError
print("########### 删除字典项 ###########")
del dict_a['four']
print(f"字典项数：{len(dict_a)}, 内容：{dict_a}") # 字典项数：3, 内容：{'one': 'a', 'two': 2, 'three': 3}


# 5  pop(key[, default]) ：
# 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。
# 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError
print("########### pop(key[, default]) ###########")
val_one = dict_a.pop("one")
val_four = dict_a.pop("four", "4") # val_one: a, val_four: 4
print(f"val_one: {val_one}, val_four: {val_four}")



# 6  keys()： 返回字典所有的key
print("########### keys()： 返回字典所有的key ###########")
dict_a_keys = dict_a.keys()
print(f"dict_a_keys: {dict_a_keys} 类型 {type(dict_a_keys)}") # dict_a_keys: dict_keys(['two', 'three']) 类型 <class 'dict_keys'>
for key in dict_a_keys:
    print(f"key: {key}")



# 7  key in d: 如果 d 中存在键 key 则返回 True，否则返回 False
print("########### 判断字典中是否包含某个key ###########")
flag1 = "one" in dict_a
flag2 = "two" in dict_a
print(f"flag1: {flag1}, flag2: {flag2}") # flag1: False, flag2: True



# 8  clear(): 移除字典中的所有元素
print("########### clear(): 移除字典中的所有元素 ###########")
dict_a.clear()
print(f"字典dict_a中的项数：{len(dict_a)}, 内容：{dict_a}") # 字典dict_a中的项数：0, 内容：{}