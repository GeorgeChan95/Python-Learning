#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/10 18:57
# @Author  : George
# @File    : 15-poly-animal.py

# 多态的实现示例

class Animal:
    def cry(self):
        pass

class Dog(Animal):
    def cry(self):
        print("小狗汪汪叫")

class Cat(Animal):
    def cry(self):
        print("小猫喵喵叫")

class Bird(Animal):
    def cry(self):
        print("小鸟喳喳叫")

class Pig(Animal):
    def cry(self):
        print("小猪航航叫")

dog = Dog()
cat = Cat()
bird = Bird()
pig = Pig()

def cry_fun(animal: Animal):
    print(f"数据类型：type{animal}")
    animal.cry()

cry_fun(dog)
cry_fun(cat)
cry_fun(bird)
cry_fun(pig)

'''
数据类型：type<__main__.Dog object at 0x0000016F56D34D70>
小狗汪汪叫
数据类型：type<__main__.Cat object at 0x0000016F56D34DA0>
小猫喵喵叫
数据类型：type<__main__.Bird object at 0x0000016F56D35100>
小鸟喳喳叫
数据类型：type<__main__.Pig object at 0x0000016F56D35130>
小猪航航叫
'''