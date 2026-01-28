#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/28 21:21
# @Author  : George
# @File    : 03_queue_process.py
import os
# 使用 Queue实现进程间通信

from multiprocessing import Process, Queue
from time import sleep

class MyProcess(Process):
    def __init__(self, name, mq):
        Process.__init__(self) # 基于类继承的方式创建进程，必须实现 __init__方法
        self.name = name
        self.mq = mq

    def run(self):
        print("当前运行进程：{} - {}".format(self.name, os.getpid()))
        # print("{} 从mq获取到内容：{}".format(self.name, self.mq.get()))
        print(f"{self.name} 从mq获取到内容 {self.mq.get()}")
        self.mq.put(self.name)
        print(f"{self.name} 结束运行")

if __name__ == '__main__':
    t_list = [] # 数组，存放自定义进程

    # 创建MQ，初始化数据
    mq = Queue()
    mq.put("1")
    mq.put("2")
    mq.put("3")

    # 循环创建进程，并给每个进程设置名称
    # 将创建的进程放入 list中，用于 .join 操作
    # 启动进程
    for i in range(3):
        p = MyProcess("p{}".format(i), mq)
        t_list.append(p)
        p.start()

    # 给每个进程 .join 操作，主进程等待自定义进程执行结束
    for t in t_list:
        t.join()


    print(f"再次获取mq内容：{mq.get()}")
    print(f"再次获取mq内容：{mq.get()}")
    print(f"再次获取mq内容：{mq.get()}")

'''
当前运行进程：p1 - 43728
当前运行进程：p0 - 12932
p1 从mq获取到内容 1
p0 从mq获取到内容 2
p1 结束运行p0 结束运行

当前运行进程：p2 - 43072
p2 从mq获取到内容 3
p2 结束运行
再次获取mq内容：p1
再次获取mq内容：p0
再次获取mq内容：p2
'''