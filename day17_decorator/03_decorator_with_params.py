#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 15:31
# @Author  : George
# @File    : 03_decorator_with_params.py

# 带参数的装饰器
# 其实就是就是在外层函数外，再套一层函数，并传参
def decorators(type):
    def outer(func):
        def inner(*args, **kwargs):
            if type == 1:
                print('执行type1')
                func(args, kwargs)
            else:
                print('执行其他类型')
                func(args, kwargs)
        return inner
    return outer

@decorators(3) # 在注解中传参，内部函数通过获取参数，执行不同的行为
def my_func(a, b):
    print(f'my_func执行参数：{a} - {b}')

if __name__ == '__main__':
    my_func(1, 2)

'''
# 打印结果：
执行其他类型
my_func执行参数：(1, 2) - {}
'''