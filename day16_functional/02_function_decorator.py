#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/12 9:25
# @Author  : George
# @File    : 02_function_decorator.py
from functools import wraps


# 装饰器函数
# 使用装饰器记录函数日志

def log(func):
    # @wraps(func) # 将原函数对象的指定属性复制给包装函数对象, 默认有 __module__、__name__、__doc__,或者通过参数选择, 如果不添加这个注解，则返回的是包装对象的 __name__, __doc__
    def with_logging(*args, **kwargs):
        print("{} was calling".format(func.__name__))
        return func(*args, **kwargs)
    return with_logging

@log # 使用定义的装饰器函数
def test(x):
    '''
    :param x: 数值参数
    :return: x * x
    '''
    return x * x

print(test.__name__)  # test   ==> 由于使用了 @wraps ，装饰器函数返回原始对象参数，如果不使用 @wraps ，则返回装饰器 with_logging 对象
# :param x: 数值参数
#     :return: x * x
print(test.__doc__)

print(test(5)) # 25
