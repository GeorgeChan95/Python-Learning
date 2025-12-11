#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/10 20:13
# @Author  : George
# @File    : 02_eq_magic_method.py


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    '''
        判断两个Person对象的内容是否相等，
        如果两个Person对象的各个属性值都一样，则返回true，反之false
    '''
    def __eq__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return (self.name == other.name and
                    self.age == other.age and
                    self.gender == other.gender)
        return False


p1 = Person('George', 20, '男')
p2 = Person('George', 20, '男')

print(f"p1 == p2 ==> ", p1 == p2) # p1 == p2 ==>  True