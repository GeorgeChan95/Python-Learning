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
    pass

def fun2():
    pass


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)

    t1.start()
    t2.start()