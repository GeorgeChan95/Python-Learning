#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/1/5 19:48
# @Author  : George
# @File    : 05_thread_lock.py

# 多线程锁
from threading import Thread
from threading import Lock
def fun1(name):
    print(f"线程{name}开始运行")
    # 获取锁
    # lock.acquire()
    with lock: # 使用with语句自动管理锁的获取和释放
        global count # 声明使用全局变量count
        for i in range(100000):
            count += 1
    # 释放锁
    # lock.release()

if __name__ == "__main__":
    lock = Lock() # 定义全局锁
    count = 0 # 定义全局参数 count，初始值0
    t_list = [] # 定义线程集合

    for i in range(20):
        t = Thread(target=fun1, args=(f"t{i+1}",))
        t.start()
        t_list.append(t)
        t.join()
    print(f"多线程计算count值为：{count}")