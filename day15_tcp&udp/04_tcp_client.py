#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/7 13:46
# @Author  : George
# @File    : 04_tcp_client.py
from socket import SOCK_STREAM, socket, AF_INET

# TCP双向通信实现-服务端

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 9988))
print("客户端已经成功连接服务端")

while True:
    msg = input(">")
    print(f"客户端发送服务端消息：{msg}")
    client_socket.send(msg.encode("utf-8"))

    receive_msg = client_socket.recv(1024).decode("utf-8")
    print(f"客户端接收到服务端消息：{receive_msg}")
    if receive_msg == "88":
        break

client_socket.close()