#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 13:28
# @Author  : George
# @File    : 10_inheritance.py

# 关于类的继承

# 人类
class Person:
    sex = None
    def eat(self):
        print("人都要吃饭")

# 学生类
class Student:
    name = None
    age = None

    def go_school(self):
        print(f"{self.name} 今年 {self.age} 要上学")

# 小学生类继承人类和学生类
class Pupil(Person, Student):
    homework = None

    def __init__(self, name, age, homework):
        self.name = name
        self.age = age
        self.homework = homework

    def do_homework(self):
        print(f"小学生: {self.name} 正在写作业: {self.homework}")

# 大学生类，继承人类和学生类
class Undergraduate(Person, Student):
    job = None

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def do_job(self):
        print(f"大学生: {self.name} 正在: {self.job}")

student1 = Pupil('小红', 12, "语文")
# 父类的父类方法
student1.eat() # 人都要吃饭
# 父类的方法
student1.go_school() # 小红 今年 12 要上学
# 子类的方法
student1.do_homework() # 小学生: 小红 正在写作业: 语文

print("----------------------------------")
student2 = Undergraduate('建国', 20, '辅导家教')
# 父类的父类方法
student2.eat() # 人都要吃饭
# 父类的方法
student2.go_school() # 建国 今年 20 要上学
# 子类的方法
student2.do_job() # 大学生: 建国 正在: 辅导家教

