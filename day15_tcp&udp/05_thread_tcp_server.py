#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/7 14:34
# @Author  : George
# @File    : 05_thread_tcp_server.py
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


# 多线程实现TCP消息的收发

def receive_info():
    while True:
        receive_data = client_socket.recv(1024).decode("utf-8")
        if receive_data == '88':
            break
        print("接收到客户端发来的消息：{}".format(receive_data))

def send_info():
    while True:
        msg = input("请输入内容：")
        client_socket.send(msg.encode("utf-8"))

if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8899))

    server_socket.listen(5)
    client_socket, client_info = server_socket.accept()
    print(f"已成功连接客户端，客户端信息：{client_info}")

    t1 = Thread(target=receive_info)
    t2 = Thread(target=send_info)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    server_socket.close()
    client_socket.close()