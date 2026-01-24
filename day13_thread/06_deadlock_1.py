#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/8 8:26
# @Author  : George
# @File    : 06_deadlock_1.py

from threading import Lock
from threading import Thread
from time import sleep

# 死锁
def fun1():
    lock1.acquire()
    print("fun1获取了lock1")
    sleep(2)
    print("fun1准备获取lock2")
    flag = lock2.acquire(True, 10)
    if flag:
        print("fun1成功获取了lock2")
        lock2.release()
        print("fun1释放了lock2")
    else:
        print("fun1没有获取lock2")
    lock1.release()

def fun2():
    lock2.acquire()
    print("fun2获取了lock2")
    print("fun2准备获取lock1")
    flag = lock1.acquire(True, 10) # 获取lock1，最多阻塞10秒，超时失败
    if flag:
        print("fun2成功获取了lock1")
        lock1.release()
        print("fun2释放了lock1")
    else:
        print("fun2没有获取lock1")
    lock2.release()
    print("fun2释放了lock2")


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)

    t1.start()
    t2.start()