#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/7 14:49
# @Author  : George
# @File    : 05_thread_tcp_client.py
from socket import SOCK_STREAM, AF_INET, socket
from threading import Thread


# 多线程实现TCP消息的收发

def receive_info():
    while True:
        receive_msg = client_socket.recv(1024).decode("utf-8")
        if receive_msg == '88':
            break
        print("客户端接收到服务端发来消息：{}".format(receive_msg))


def send_info():
    while True:
        msg = input("请输入内容：")
        client_socket.send(msg.encode("utf-8"))

if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8899))
    print("客户端成功连接了服务端")
    
    t1 = Thread(target=receive_info)
    t2 = Thread(target=send_info)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    client_socket.close()