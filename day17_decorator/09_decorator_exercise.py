#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 16:44
# @Author  : George
# @File    : 09_decorator_exercise.py
import time


# 缓存装饰器和计时装饰器综合练习
# 实现函数执行结果缓存和计时的装饰器功能

class CacheDecorator:
    __cache = {}  # 字典参数，缓存结果，以函数名称为key
    '''
    缓存装饰器
    '''

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if self.func.__name__ in CacheDecorator.__cache:  # 判断函数名称是否已在 __cache 中
            # 如果缓存命中，从缓存中获取结果
            result = CacheDecorator.__cache.get(self.func.__name__)
            return result
        else:
            # 如果缓存中不存在，则调用func，获取结果
            result = self.func(*args, **kwargs)
            # 将结果存储在缓存中
            CacheDecorator.__cache[self.func.__name__] = result
            return result


def log_decorator(func):
    '''
    日志装饰器
    :param func:
    :return:
    '''

    def log_inner(*args, **kwargs):
        print("日志记录.....")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"执行方法用时：{end - start} 秒")

    return log_inner


@log_decorator
@CacheDecorator
def my_func():
    time.sleep(3)
    return 999


if __name__ == '__main__':
    my_func()
    my_func()
'''
运行打印如下：
日志记录.....
执行方法用时：3.0007951259613037 秒
日志记录.....
执行方法用时：0.0 秒
'''
