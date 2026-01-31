#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 14:06
# @Author  : George
# @File    : 05_manager_process.py
import multiprocessing
import os
from multiprocessing import Manager


# 使用Manager() 实现在主进程和子进程之间进行参数的传递

def fun1(name, mList, mDict):
    print(f"当前进程号：{os.getpid()}, 父进程号：{os.getppid()},进程名称：{name}, 获取到初始参数 mList:{mList}, mDict:{mDict}")
    mList.append("abc")
    mDict['age'] = 20

if __name__ == '__main__':
    print(f"主进程开始运行，进程号：{os.getpid()}")
    with Manager() as mgr:
        m_list = mgr.list() # 数组
        m_dict = mgr.dict() # 字典
        m_list.append("123")
        m_dict['name'] = 'George'

        p1 = multiprocessing.Process(target=fun1, args=('p1', m_list, m_dict))
        p1.start()
        p1.join()

        print(f"子进程运行结束，m_list: {m_list}, m_dict: {m_dict}")

'''
主进程开始运行，进程号：11180
当前进程号：30496, 父进程号：11180,进程名称：p1, 获取到初始参数 mList:['123'], mDict:{'name': 'George'}
子进程运行结束，m_list: ['123', 'abc'], m_dict: {'name': 'George', 'age': 20}
'''