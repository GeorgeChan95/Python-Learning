#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/4 11:03
# @Author  : George
# @File    : 01_feet_cat_oop.py

# 定义类和属性的默认值
class Cat:
    age = 1
    name = '大壮'
    color = '黑色'
    weight = 10

# 创建实例对象
cat1 = Cat()

print(f"我有一只{cat1.color}的{cat1.age}岁的猫叫做：{cat1.name}，它重{cat1.weight}kg") # 我有一只白色的2岁的猫叫做：小白，它重5.0kg
