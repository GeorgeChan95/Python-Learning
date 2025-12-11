#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/11 19:47
# @Author  : George
# @File    : 05_abstract_class_test.py

'''
1. 抽象类不能被实例化
2。 抽象类需要继承ABC，并且需要至少一个抽象方法
3. 抽象类中可以有普通方法
4. 如果一个类继承了抽象类，则它必须实现所有的抽象方法，否则它还是一个抽象类
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义首相方法
    @abstractmethod
    def cry(self):
        pass

# 注意:抽象类(含有抽象方法), 不能实例化
# TypeError: Can't instantiate abstract class Animal
# animal = Animal("动物", 3)

# 编写子类Tiger 继承 Animal 并实现抽象方法
class Tiger(Animal):
    def cry(self):
        print(f"老虎 {self.name} 嗷嗷叫...")

tiger = Tiger("泰哥", 2)
tiger.cry() # 老虎 泰哥 嗷嗷叫...