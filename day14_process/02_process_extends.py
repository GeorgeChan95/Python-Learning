#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/27 19:31
# @Author  : George
# @File    : 02_process_extends.py
import os
from multiprocessing import Process
from time import sleep


# 创建进程，通过继承的形式

class MyProcess(Process):
    def __init__(self, name): # 进程的名称需要以构造函数方式传参
        Process.__init__(self)
        self.name = name

    def run(self):
        print("当前进程号：{}".format(os.getpid()))
        print("当前父进程号：{}".format(os.getppid()))
        print(f"{self.name} 开始执行")
        sleep(3)
        print(f"{self.name} 结束执行")

if __name__ == '__main__':
    print("当前主线程进程号：{}".format(os.getpid()))
    print("当前主线程父进程号：{}".format(os.getppid()))
    p1 = MyProcess("p1")
    p2 = MyProcess("p2")
    p1.start()
    p2.start()

'''
当前主线程进程号：35284
当前主线程父进程号：13940
当前进程号：35392
当前父进程号：35284
p1 开始执行
当前进程号：3720
当前父进程号：35284
p2 开始执行
p1 结束执行
p2 结束执行
'''