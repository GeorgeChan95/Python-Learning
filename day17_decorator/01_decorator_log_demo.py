#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 14:25
# @Author  : George
# @File    : 01_decorator_log_demo.py

# 使用装饰器实现日志功能

def out_log(func):
    '''基于闭包实现给函数添加日志打印功能'''
    def inner(*args, **kwargs):
        # 打印日志
        print(f"打印参数：{args} -- {kwargs}")
        # 调用函数
        func(*args, **kwargs)
    # 返回内部函数
    return inner

@out_log # 使用 @ + 加函数名，表示给函数添加装饰器
def fun1(a, b):
    print("执行fun1函数")

# 方式1，使用 args 传参， 打印内容：打印参数：(100, {'name': 'tom'}) -- {}
fun1(100, {'name': 'tom'})

print("====== 分割线 ======")
# 方式2，使用关键字传参，打印内容：打印参数：() -- {'a': 100, 'b': {'name': 'tom'}}
args = ()
kwargs = {'a': 100, 'b': {'name': 'tom'}}
fun1(*args, **kwargs)
