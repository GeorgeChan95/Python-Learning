#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 10:43
# @Author  : George
# @File    : 10_pickle.py

# 序列化和反序列化模块
import pickle

# 对象序列化到文件中
with open("data.dat", "wb") as f:
    name = "George"
    age = 30
    score = 80.3
    resume = {'name': name, 'age': age, 'score': score}
    pickle.dump(resume, f)
    print("已成功将内容序列化到文件中")

# 文件反序列化到对象
with open("data.dat", "rb") as f:
    resume = pickle.load(f)
    print(f"从文件中反序列化，读取到对象为：{resume}") # 从文件中反序列化，读取到对象为：{'name': 'George', 'age': 30, 'score': 80.3}