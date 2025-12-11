#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/11 19:14
# @Author  : George
# @File    : 03_class_object.py

class Monster:
    name = "蝎子精"
    age = 300

    def hi(self):
        print(f'hi() {self.name}-{self.age}')

print(Monster) # <class '__main__.Monster'>

# 通过Class对象, 可以引用属性 (没有创建实例对象也可以引用/访问)
print(f"{Monster.name}----{Monster.age}") # 蝎子精----300

# 通过类名如何调用非静态成员方法
Monster.hi(Monster) # hi() 蝎子精-300