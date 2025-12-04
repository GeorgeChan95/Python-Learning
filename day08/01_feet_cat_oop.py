#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/4 11:03
# @Author  : George
# @File    : 01_feet_cat_oop.py

# 定义类和属性的默认值
class Cat:
    age = None
    name = None
    color = None
    weight = None

# 创建实例对象
cat1 = Cat()
cat1.age = 2
cat1.name = "小白"
cat1.weight = 5.0
cat1.color = "白色"

print(f"我有一只{cat1.color}的{cat1.age}岁的猫叫做：{cat1.name}，它重{cat1.weight}kg") # 我有一只白色的2岁的猫叫做：小白，它重5.0kg


cat2 = Cat()
print(bool(cat2)) # True
cat2 = None
print(bool(cat2)) # False