#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/25 21:13
# @Author  : George
# @File    : 09_event.py
import threading
from threading import Event
from time import sleep


# 事件 Event

def car():
    num = 0 # 车上人员初始为0
    while True:
        if event.is_set():
            print("车已经到站了，开始上车")
            sleep(1)
            num += 1
            print(f"已上车人数：{num}")
            if num % 5 == 0:
                event.clear() # 上满5个人就等一会, event 标志设置成 False
        else:
            print("公交开始发车")
            sleep(6)
            event.set() # 事件标志设置成True，线程放行


def person():
    num = 0
    while True:
        if event.is_set(): # 判断事件标志是否为 True， 如果为 True，人员开始上车
            num += 1
            print(f"第 {num} 人上车")
            sleep(1)
        else:
            event.wait(timeout=None)


if __name__ == '__main__':
    event = Event()

    t1 = threading.Thread(target=car)
    t2 = threading.Thread(target=person)

    t1.start()
    t2.start()