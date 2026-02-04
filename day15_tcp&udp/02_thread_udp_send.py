#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/4 10:53
# @Author  : George
# @File    : 02_thread_udp_send.py
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread


# 使用多线程完成数据的收和发

def sendData():
    s = socket(AF_INET, SOCK_DGRAM)
    # s.bind(('127.0.0.1', 9988))
    addr = ('127.0.0.1', 9988)

    while True:
        data = input("请输入内容：")
        s.sendto(data.encode("utf-8"), addr)

def receiveData():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('127.0.0.1', 8899))
    while True:
        data = s.recvfrom(1024)
        print(f"接收到消息内容：{data[0].decode('utf-8')}, 消息发送发：{data[1]}")




if __name__ == '__main__':
    t1 = Thread(target=sendData)
    t2 = Thread(target=receiveData)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
