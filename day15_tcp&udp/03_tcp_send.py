#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/4 19:23
# @Author  : George
# @File    : 03_tcp_send.py

# 使用TCP完成消息的收发
# 服务端实现

from socket import AF_INET, SOCK_STREAM, socket

# 建立服务端socket

# AF_INET：表示使用 IPv4 地址（如 127.0.0.1）
# SOCK_STREAM：表示使用 TCP 协议（流式传输）
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定IP和端口
server_socket.bind(("127.0.0.1", 8899)) # 127.0.0.1：本机回环地址，只能本机访问， 如果希望局域网其他机器也能访问，应绑定： server_socket.bind(("0.0.0.0", 8899))
# 监听连接，参数 5 表示：最大等待连接队列长度（排队人数）。
# 如果同时有多个客户端连接，最多允许 5 个在队列中排队等待 accept。
# 服务器一次只能 accept() 一个连接，但如果同时来了很多连接请求，操作系统会帮你先排队。
server_socket.listen(5)
# 等待客户端连接（阻塞）
# client_socket 用来和这个客户端通信的 socket（专用连接通道）
# client_info 客户端的地址信息，通常是一个元组 ('客户端IP', 客户端端口)
client_socket, client_info = server_socket.accept()
# 接收客户端发送的数据, 一次最多接收 1024 字节（1KB）
recv_data = client_socket.recv(1024)
print(f"接收到消息：{recv_data.decode('utf-8')}，来自：{client_info}")
# 关闭与客户端的连接。
client_socket.close()
# 关闭服务端 socket
server_socket.close()
