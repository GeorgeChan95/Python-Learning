#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/11 19:20
# @Author  : George
# @File    : 04_staticmethod.py

class Monster:
    name = 'jack'
    age = 20

    @staticmethod # 标记为静态方法
    def hi():
        print(f"{Monster.name}------{Monster.age}") # 静态方法没有 self，直接 类名.属性名 调用

# 通过类名直接调用静态方法
Monster.hi() # jack------20

# 通过示例对象调用静态方法
monster = Monster()
monster.hi() # jack------20