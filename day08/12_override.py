#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 14:58
# @Author  : George
# @File    : 12_override.py

# 父类Person
class Person:
    name = '111'
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"名字:{self.name} 年龄:{self.age}"


# 子类Student
class Student(Person):
    id = None
    score = None

    def __init__(self, id, score, name, age):
        # 调用父类的构造器完成继承父类的属性的初始化
        super().__init__(name, age)
        print(super().name) # 获取super()父类的属性，可以操作
        # super().name = name # 通过super()设置父类的属性，这是不允许的
        # 子类的特有的属性，我们自己完成初始化
        self.id = id
        self.score = score

    def say(self):
        return f"id:{self.id} 成绩:{self.score} {super().say()}, {super().name}"

p1 = Person('tom', 20)
print(p1.say()) # 名字:tom 年龄:20

s1 = Student(2, 99, 'jerry', 30)
print(s1.say()) # id:2 成绩:99 名字:jerry 年龄:30, 111
