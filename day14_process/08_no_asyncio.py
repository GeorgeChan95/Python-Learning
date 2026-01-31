#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 16:38
# @Author  : George
# @File    : 08_no_asyncio.py
import time
from time import sleep

# 不使用协程，测试程序的执行时长

def fun1():
    for i in range(3):
        print(f"去北京第：{i + 1} 次")
        sleep(1)
    return "fun1执行完毕"

def fun2():
    for i in range(3):
        print(f"去上海第：{i + 1} 次")
        sleep(1)
    return "fun2执行完毕"

def main():
    fun1()
    fun2()

if __name__ == '__main__':
    star_time = time.time()
    main()
    end_time = time.time()
    print(f"不使用协程，程序执行耗时：{end_time - star_time}")

'''
去北京第：1 次
去北京第：2 次
去北京第：3 次
去上海第：1 次
去上海第：2 次
去上海第：3 次
不使用协程，程序执行耗时：6.0020904541015625
'''