#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/4 20:09
# @Author  : George
# @File    : 05_self.py


class Dog:
    name = "波比"
    age = 2

    def info(self, name):
        print(f"name信息: {name}")  # name信息: 史努比
        # 通过self.属性名 可以访问 对象的属性/成员变量
        print(f"属性name: {self.name}") # 属性name: 波比


dog = Dog()
dog.info("史努比")


class Cat:
    name = "小花"


    @staticmethod
    def call(name):
        print(f"小猫的名字：{name}")

    @staticmethod
    def call02(self, name):
        print(f"小猫的名字：{self.name}, 别名：{name}")

cat = Cat()
cat.call("小红") # 小猫的名字：小红

Cat.call("小黑") # 小猫的名字：小黑

Cat.call02(cat, "小白") # 小猫的名字：小花, 别名：小白
