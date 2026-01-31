#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 16:09
# @Author  : George
# @File    : 07_with_pool_process.py

# 使用with 字段管理 Pool线程池资源

import os
from multiprocessing import Pool
from time import sleep


# 使用进程池实现多进程

def fun1(name):
    print(f"当前执行的进程id: {os.getpid()}, 进程名称：{name}")
    sleep(2)
    return name + "_1"

def fun2(params): # fun2的参数，来自于 fun1 的返回
    print(f"接收到：{params}")

if __name__ == '__main__':
    with Pool(5) as pool:
        args = pool.map(fun1, ('poo1','poo2','poo3','poo4','poo5','poo6','poo7'))
        for arg in args:
            print(arg)

'''
当前执行的进程id: 20904, 进程名称：poo1
当前执行的进程id: 12032, 进程名称：poo2
当前执行的进程id: 6424, 进程名称：poo3
当前执行的进程id: 25576, 进程名称：poo4
当前执行的进程id: 7440, 进程名称：poo5
当前执行的进程id: 20904, 进程名称：poo6
当前执行的进程id: 6424, 进程名称：poo7
poo1_1
poo2_1
poo3_1
poo4_1
poo5_1
poo6_1
poo7_1
'''