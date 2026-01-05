#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/1/5 19:10
# @Author  : George
# @File    : 01_thread_base.py

from threading import Thread
from time import sleep

# 通过方法包装实现一个多线程

def fun1(name):
    print(f"线程：{name} 开始执行")
    sleep(3) # 暂停线程3秒

if __name__ == "__main__":
    # 创建线程
    t1 = Thread(target=fun1, args=("t1",)) # 注意参数的传递是一个元组，如果只有一个参数，最后要加逗号，
    t2 = Thread(target=fun1, args=("t2",))

    # 启动线程
    t1.start()
    t2.start()
