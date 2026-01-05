#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/1/5 19:40
# @Author  : George
# @File    : 04_thread_daemon.py

# 守护线程

from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"{self.name}开始运行")
        sleep(30)
        print(f"{self.name}结束运行")

if __name__ == "__main__":
    for i in range(20):
        t = MyThread(f"t{i+1}")
        # 设置线程为守护线程，如果main线程结束运行，守护线程也会跟着结束
        t.daemon = True
        t.start()

    print("主线程运行结束")

'''
t1开始运行
t2开始运行
t3开始运行
t4开始运行
t5开始运行
t6开始运行
t7开始运行
t8开始运行
t9开始运行
t10开始运行
t11开始运行
t12开始运行
t13开始运行
t14开始运行
t15开始运行
t16开始运行
t17开始运行
t18开始运行
t19开始运行
t20开始运行主线程运行结束
'''
# 主线程运行结束，其它所有守护线程都立即停止了运行