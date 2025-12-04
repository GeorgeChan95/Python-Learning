#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/4 11:21
# @Author  : George
# @File    : 03_obj_ref_pass.py

# 对象的引用传递

class Person:
    name = None
    age = None

person1 = Person()
person1.name = "张三"
person1.age = 20

# person2也指向person1
person2 = person1

print(f"person1的地址：{id(person1)},  person2的地址：{id(person2)}") # person1的地址：2396398176640,  person2的地址：2396398176640
print(f"person2的属性值，name={person2.name}, age={person2.age}") # person2的属性值，name=张三, age=20


person2 = Person()
print(f"person1的地址：{id(person1)},  person2的地址：{id(person2)}") # person1的地址：2396398176640,  person2的地址：2396398176688
print(f"person2的属性值，name={person2.name}, age={person2.age}") # person2的属性值，name=None, age=None