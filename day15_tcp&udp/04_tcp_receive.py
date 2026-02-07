#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/4 19:23
# @Author  : George
# @File    : 04_tcp_receive.py
from socket import SOCK_STREAM, AF_INET, socket

# 使用TCP完成消息的收发
# 客户端实现

# 1.建立Socket连接， SOCK_STREAM 表示TCP连接, AF_INET 表示表示IPV4
client_socket = socket(AF_INET, SOCK_STREAM)
# 2.建立与服务端的连接，服务端地址 127.0.0.1， 端口 8899,注意是 元组格式
client_socket.connect(("127.0.0.1", 8899))
# 3.向服务端发送消息 ‘你好’， 消息使用 utf-8 编码
client_socket.send("你好".encode("utf-8"))
# 4.关闭与服务端的连接
client_socket.close()