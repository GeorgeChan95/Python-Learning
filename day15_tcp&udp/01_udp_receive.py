#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/4 10:22
# @Author  : George
# @File    : 01_udp_receive.py
from socket import socket, SOCK_DGRAM, AF_INET

# UDP 接收消息
s = socket(AF_INET, SOCK_DGRAM)
addr = ('127.0.0.1', 9090)
s.bind(addr)

# data = input("请输入：")
# s.sendto(data.encode('utf-8'), addr)

# 等待接收数据
res = s.recvfrom(1024) # 1024是一次接收的最大字节数
print(res[0].decode("utf-8"))

# 关闭socket
s.close()