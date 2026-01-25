#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/24 15:13
# @Author  : George
# @File    : 07_recursive_lock.py
import threading
from threading import Lock, RLock, Thread


# 递归锁 RLock

def fun1():
    rlock.acquire()
    t = threading.current_thread()
    threadName = t.name
    print(f"fun1第一次获取锁, 线程名称：{threadName}")
    fun2()
    rlock.release()
    print("fun1释放了锁")

def fun2():
    rlock.acquire()
    t = threading.current_thread()
    threadName = t.name
    print(f"fun2获取了锁, 线程名称：{threadName}")
    rlock.release()
    print("fun2释放了锁")


def fun3():
    t = threading.current_thread()
    threadName = t.name
    print(f"fun3执行中，当前线程：{threadName}")
    fun1()
    fun2()

if __name__ == '__main__':
    # lock = Lock() 不可重入锁，同一个线程重复获取锁会阻塞
    rlock = RLock() # 可重入锁 ，同一个线程可以重复获取锁

    t = Thread(target=fun3, name="t3")
    t.start()
    t.join()

'''
fun3执行中，当前线程：t3
fun1第一次获取锁, 线程名称：t3
fun2获取了锁, 线程名称：t3
fun2释放了锁
fun1释放了锁
fun2获取了锁, 线程名称：t3
fun2释放了锁
'''