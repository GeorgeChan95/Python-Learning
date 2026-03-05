#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 20:01
# @Author  : George
# @File    : 09_dataclass.py

# dataclass 新特性

'''
@dataclass：数据类装饰器，自动生成__init__、__repr__等方法
dataclass 是 Python 3.7 引入的一个新特性，用于自动生成类的特殊方法，如 __init__、__repr__ 等。

field()：字段配置函数，用于定制单个字段的行为，如默认值、是否包含在 repr 中等。

ClassVar：类型提示，标记类变量（不是实例变量）, 类变量在所有实例之间共享，而实例变量每个实例都有一个副本。

'''

from  dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Player:
    name:str # # 必需字段，无默认值
    postion:str # # 必需字段，无默认值
    age:int # # 必需字段，无默认值
    sex:str=field(default='man',repr=False) # 可选字段，默认值为 'man'，不包含在 repr 中， # 打印对象不显示
    # msg:str=field(default='')
    msg:str=field(default_factory=str) #  使用str()函数生成默认值,每次创建实例时，都会调用str()生成空字符串'', 相比default=''，default_factory会创建新的字符串对象
    #类变量
    country:ClassVar[str] # 标记为类变量（不属于实例）,不会被包含在数据类自动生成的方法中, 所有实例共享同一个值

#创建实例对象
p = Player('zs','北京',24)
print(p) # Player(name='zs', postion='北京', age=24, msg='')

# 给类变量 country 赋值
Player.country = '中国'
print('类属性：',Player.country)