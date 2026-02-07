#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/7 13:39
# @Author  : George
# @File    : 04_tcp_server.py
from socket import socket, AF_INET, SOCK_STREAM

# TCP双向通信实现-服务端

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9988))

# 监听客户端连接
server_socket.listen(5)
print('服务端已经启动，等待客户端连接')
client_socket, client_info = server_socket.accept()
print(f"客户端连接成功，客户端信息：{client_info}")
while True:
    receive_msg = client_socket.recv(1024).decode("utf-8")
    print(f"接收到客户端发送过来的信息：{receive_msg}")

    if receive_msg == '88':
        break

    send_msg = input(">")
    client_socket.send(send_msg.encode("utf-8"))

client_socket.close()
server_socket.close()