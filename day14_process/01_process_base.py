#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/27 19:21
# @Author  : George
# @File    : 01_process_base.py

# 进程的基础使用

from multiprocessing import Process
from time import sleep

def fun1(name):
    print(f"{name}执行开始")
    sleep(3)
    print(f"{name}执行结束")

if __name__ == '__main__':
    # 创建线程
    p1 = Process(target=fun1, args=("P1",)) # args 为字典
    p2 = Process(target=fun1, args=("P2",))
    p1.start()
    p2.start()