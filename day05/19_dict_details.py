#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/30 10:54
# @Author  : George
# @File    : 19_dict_details.py

# 字典的使用明细

# 1字典的Key(关键字)通常是字符串或数字, Value可以是任意数据类型
print("########### 定义字典 ###########")
dict_a = {
    "jack": [100, 200, 300],
    "mary": (10, 20, "hello"),
    "nono": {"apple", "pear"},
    "smith": "计算机老师",
    "周星驰": {
        "性别": "男",
        "age": 18,
        "地址": "香港"
    },
    "key1": 100,
    "key2": 9.8,
    "key3": True,
    100: "height"
}
print(f"dict_a: {dict_a} 类型: {type(dict_a)}") # dict_a: {'jack': [100, 200, 300], 'mary': (10, 20, 'hello'), 'nono': {'apple', 'pear'}, 'smith': '计算机老师', '周星驰': {'性别': '男', 'age': 18, '地址': '香港'}, 'key1': 100, 'key2': 9.8, 'key3': True, 100: 'height'} 类型: <class 'dict'>


# 2、字典不支持索引
print("########### 字典不支持索引 ###########")
# print(dict_a[0]) # 报错：KeyError: 0
r'''
Traceback (most recent call last):
  File "E:\study\PythonLearning\Python-Learning\day05\19_dict_details.py", line 31, in <module>
    print(dict_a[0])
          ~~~~~~^^^
KeyError: 0
'''



# 3、既然字典不支持索引, 所以对字典进行遍历不支持while , 只支持for
print("########### 字典的循环 ###########")
# 方式一
print("########### 方式一 ###########")
for key in dict_a:
    print(f"key: {key}, value: {dict_a[key]}")

# 方式二
print("########### 方式二 ###########")
for value in dict_a.values():
    print(f"value: {value}")

# 方式三
print("########### 方式三 ###########")
for key, value in dict_a.items():
    print(f"key: {key}, value: {dict_a[key]}")


# 4、创建空字典可以通过{}，或者 dict()
print("########### 创建空字典 ###########")
dict_b = dict()
dict_c = {}
print(f"dict_b: {dict_b} 类型: {type(dict_b)}")  # dict_b: {} 类型: <class 'dict'>
print(f"dict_c: {dict_c} 类型: {type(dict_c)}")  # dict_c: {} 类型: <class 'dict'>


# 5、字典的key必须是唯一的, 如果你指定了多个相同的key , 后面的键值对会覆盖前面的
print("########### 字典的key必须是唯一的 ###########")
dict_e = {'one': 1, 'two': 2, 'three': 3, 'two': 200}
print(f"dict_e: {dict_e}")  # dict_e: {'one': 1, 'two': 200, 'three': 3}