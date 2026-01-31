#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 15:50
# @Author  : George
# @File    : 06_pool_process.py
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
    pool = Pool(5) # 创建进程池

    pool.apply_async(func=fun1, args=('poo1',), callback=fun2) # args 是用来给fun1传参，
    pool.apply_async(func=fun1, args=('poo2',), callback=fun2)
    pool.apply_async(func=fun1, args=('poo3',), callback=fun2)
    pool.apply_async(func=fun1, args=('poo4',), callback=fun2)
    pool.apply_async(func=fun1, args=('poo5',), callback=fun2)
    pool.apply_async(func=fun1, args=('poo6',), callback=fun2)
    pool.apply_async(func=fun1, args=('poo7',), callback=fun2)

    pool.close()
    pool.join()
