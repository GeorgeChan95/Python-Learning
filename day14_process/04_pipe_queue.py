#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 13:21
# @Author  : George
# @File    : 04_pipe_queue.py
import multiprocessing
import os

# 基于Pipe实现进程间通讯

def fun1(conn1):
    print(f"当前进程号：{os.getpid()},发送消息：{'你好'}")
    conn1.send('你好')
    info = conn1.recv()
    print(f"当前进程号：{os.getpid()},接收到消息：{info}")

def fun2(conn2):
    print(f"当前进程号：{os.getpid()},发送消息：{'Hello'}")
    conn2.send('Hello')
    info = conn2.recv()
    print(f"当前进程号：{os.getpid()},接收到消息：{info}")

if __name__ == '__main__':
    conn1, conn2 = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=fun1, args=(conn1,))
    p2 = multiprocessing.Process(target=fun2, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

'''
当前进程号：23676,发送消息：你好
当前进程号：12192,发送消息：Hello
当前进程号：12192,接收到消息：你好
当前进程号：23676,接收到消息：Hello
'''