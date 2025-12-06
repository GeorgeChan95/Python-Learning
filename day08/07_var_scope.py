#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 10:24
# @Author  : George
# @File    : 07_var_scope.py

# 属性的作用域

class Cat:
    # 属性
    name = None
    age = None

    # n1,n2, result 就是局部变量
    def cal(self, n1, n2):
        result = n1 + n2
        print(f"result={result}")
        print(f"cal() 使用属性 name {self.name}") # None

    def cry(self):
        print(f"cry() 使用 属性name {self.name}") # None

    def eat(self):
        print(f"eat() 使用 属性name {self.name}") # None


cat = Cat()
cat.cal(10, 20)
cat.cry()
cat.eat()