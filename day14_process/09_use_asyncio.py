#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 16:43
# @Author  : George
# @File    : 09_use_asyncio.py
import asyncio
import time


# 使用 asynco 实现协程

# 定义异步函数（协程函数），会返回一个协程对象
async def fun1():
    for i in range(3):
        print(f"去北京第：{i + 1} 次")
        await asyncio.sleep(1) # 异步等待，交出控制权，让其他协程可以执行
    return "fun1执行完毕"

async def fun2():
    for i in range(3):
        print(f"去上海第：{i + 1} 次")
        await asyncio.sleep(1)
    return "fun2执行完毕"

async def main():
    await asyncio.gather(fun1(), fun2()) # 并发执行多个协程，等待所有完成

if __name__ == '__main__':
    star_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"使用协程，程序执行耗时：{end_time - star_time}")

'''
去北京第：1 次
去上海第：1 次
去北京第：2 次
去上海第：2 次
去北京第：3 次
去上海第：3 次
使用协程，程序执行耗时：3.01369571685791
'''