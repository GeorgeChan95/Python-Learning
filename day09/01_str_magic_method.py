#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/10 20:03
# @Author  : George
# @File    : 01_str_magic_method.py

class Monster:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    """
        1. 在默认情况下,调用的是父类object的__str__
        2.父类object的__str__ 返回的就是类型+地址
        3.可以根据需要重写__str__ 
        
        其实就是Java中重写 ToString方法
    """
    def __str__(self):
        # return super().__str__()
        return f"{self.name} {self.age} {self.gender}"


m = Monster("青牛怪", 500, '男')

print(m)  # 默认输出类型+对象的地址