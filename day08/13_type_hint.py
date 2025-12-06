#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 15:28
# @Author  : George
# @File    : 13_type_hint.py

# 函数传参的类型注解
def fun(var: str):
    for ele in var:
        print(ele)


# ctrl+p 提示参数时, 没有类型提示
# 如果类型传错了, 就会出现异常
fun('100')

list1: list = [1, 2, 3]
my_tuple: tuple = (1, '2', 0.9)
print(my_tuple)

# 容器类型注解
my_list2: list[int] = [100, 200, 300]
# 元组类型设置详细类型注解, 需要把每个元素类型都标注一下
my_tuple2: tuple[str, str, str, float] = ("run", "sing", "fly", 1.1)
my_set2: set[str] = {"jack", "tim", "hsp"}
# 字典类型设置详细类型注解, 需要设置两个类型, 即[key类型, value类型]
# my_dict2: dict[str, int]: 对my_dict2进行类型注解, 标注my_dict2类型是dict, 而且
# key的类型是str, values的类型是int
my_dict2: dict[str, int] = {"no1": 100, "no2": 200}


# 对函数（方法）返回值类型注解
def fun2(a: int, b: int) -> int:
    return a + b


# fun2('a', 2)
