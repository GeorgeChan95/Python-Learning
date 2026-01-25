#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/25 22:11
# @Author  : George
# @File    : 10_queue.py
from queue import Queue
from threading import Thread
from time import sleep


# 队列 Queue，生产者、消费者模型

def producer(): # 生产者
    num = 1
    while True:
        if queue.qsize() < 5:
            print(f"生产第{num}个产品")
            queue.put(num)
            num += 1
        else:
            print("等待消费")
            sleep(1)

def consumer(): # 消费者
    while True:
        if queue.qsize() > 0:
            print(f"消费第{queue.get()}个产品")

if __name__ == '__main__':
    queue = Queue() # 创建消息队列
    p1 = Thread(target=producer) # 1个消息生产者
    p1.start()

    c1 = Thread(target=consumer) # 2个消费者
    c1.start()

    c2 = Thread(target=consumer)
    c2.start()