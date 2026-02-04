#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/4 9:57
# @Author  : George
# @File    : 01_udp_send.py
from socket import SOCK_DGRAM, AF_INET, socket

# 使用UDP发送数据

# AF_INET 使用 IPv4 地址
# SOCK_DGRAM 使用 UDP 协议
s = socket(AF_INET, SOCK_DGRAM)
# 定义目标主机地址（服务器地址）
addr = ('127.0.0.1', 9090)
# 从控制台获取输入内容
data = input("请输入内容：")
# 使用udp发送消息
s.sendto(data.encode("utf-8"), addr)
# 主动断开socket
s.close()
