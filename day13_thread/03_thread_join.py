#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/1/5 19:33
# @Author  : George
# @File    : 03_thread_join.py

# 线程的join方法

from threading import Thread
from time import sleep

def fun1(name):
    print(f"{name} 开始执行")
    sleep(2)
    print(f"{name} 执行完毕")

if __name__ == "__main__":
    t1 = Thread(target=fun1, args=("线程1",))
    t2 = Thread(target=fun1, args=("线程2",))
    t1.start()
    t2.start()
    t1.join() # 等待线程1执行完毕, 主线程会阻塞在这里, 直到线程1执行完毕
    t2.join() # 等待线程2执行完毕
    print("所有线程执行完毕")
