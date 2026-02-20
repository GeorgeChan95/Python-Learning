#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 15:42
# @Author  : George
# @File    : 04_decorator_wraps.py
from functools import wraps


# @wraps(func) # 将原函数对象的指定属性复制给包装函数对象, 默认有 __module__、__name__、__doc__,
# 或者通过参数选择, 如果不添加这个注解，则返回的是包装对象的 __name__, __doc__

def log(func):
    # @wraps(func)
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
print("==============1111===============")
# :param x: 数值参数
#     :return: x * x
print(test.__doc__)
print("==============2222===============")

print(test(5)) # 25

'''
日志打印如下：
        --- 添加了 @wraps(func)
        test
        ==============1111===============
        
            :param x: 数值参数
            :return: x * x
            
        ==============2222===============
        test was calling
        25
        
        
        --- 没有添加了 @wraps(func)
        with_logging
        ==============1111===============
        None
        ==============2222===============
        test was calling
        25
'''

