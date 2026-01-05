#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/1/5 19:24
# @Author  : George
# @File    : 02_thread_create_class.py

# 基于类实现多线程

from threading import Thread
from time import sleep

class MyThread(Thread): # 继承Thread类
    def __init__(self, name, delay):
        Thread.__init__(self) # 调用父类的初始化方法， 初始化线程的属性，如name, daemon等， 并设置线程的名称为name， 默认为Thread-1, Thread-2等
        self.name = name # 设置线程的名称为name
        self.delay = delay # 设置线程的延迟时间为delay

    def run(self):
        print(f"{self.name} 开始执行")
        sleep(self.delay)
        print(f"{self.name} 执行完毕")

if __name__ == "__main__":
    t1 = MyThread("线程1", 2)
    t2 = MyThread("线程2", 3)
    t1.start()
    t2.start()

'''
线程1 开始执行
线程2 开始执行
线程1 执行完毕
线程2 执行完毕
'''