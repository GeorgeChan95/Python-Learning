#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/10 19:09
# @Author  : George
# @File    : 02-master-feed-animal.py

# 多态案例2：给动物喂食

class Food:
    name = None
    def __init__(self, name: str):
        self.name = name

class Fish(Food):
    # 特有的属性和方法
    pass

class Bone(Food):
    # 特有的属性和方法
    pass


class Animal:
    name = None
    def __init__(self, name: str):
        self.name = name

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Master:
    name = None
    def __init__(self, name: str):
        self.name = name

    def feed(self, animal: Animal, food: Food):
        print(f"主人{self.name}给动物：{animal.name}喂的食物是：{food.name}")


fish = Fish("草鱼")
bone = Bone("骨头")

cat = Cat("咪咪")
dog = Dog("旺财")

master = Master("乔治")
master2 = Master("露露")

master.feed(cat, fish)
master2.feed(dog, bone)

'''
主人乔治给动物：咪咪喂的食物是：草鱼
主人露露给动物：旺财喂的食物是：骨头
'''