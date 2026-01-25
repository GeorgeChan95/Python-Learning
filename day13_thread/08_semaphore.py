#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/25 16:26
# @Author  : George
# @File    : 08_semaphore.py
import threading
from multiprocessing import Semaphore
from threading import Thread
from time import sleep


# 信号量
def fun1(name):
    se.acquire() # 获取锁
    t_name = threading.current_thread().name
    print(f"当前线程为：{t_name}")
    sleep(2)
    se.release() # 释放锁

def fun2(name, se):
    se.acquire()  # 获取锁
    t_name = threading.current_thread().name
    print(f"当前线程为：{t_name}")
    sleep(2)
    se.release()  # 释放锁

if __name__ == '__main__':
    se = Semaphore(3) # 信号量,同时只允许3个线程获得锁
    list = []

    for i in range(0, 10):
        name = f"t_{i}"
        t1 = Thread(target=fun1, args=(name,), name=f"{name}")
        list.append(t1)
        t1.start()

    for t in list: # 子线程结束后，主线程才能结束
        t.join()
    print("主线程结束")