#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/30 10:45
# @Author  : George
# @File    : 18_dict_define.py

# 字典的定义
dict1 = {"name": "zhangsan", "age": 20}
dict2 = {18: "wilde", 20: "height"}
print(f"数据类型：{type(dict1)}, 内容：{dict1}") # 数据类型：<class 'dict'>, 内容：{'name': 'zhangsan', 'age': 20}
print(f"人员姓名：{dict1["name"]}")
print(f"数据类型：{type(dict2)}, 内容：{dict2}") # 数据类型：<class 'dict'>, 内容：{18: 'wilde', 20: 'height'}
