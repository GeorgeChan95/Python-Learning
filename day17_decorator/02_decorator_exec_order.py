#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/20 15:05
# @Author  : George
# @File    : 02_decorator_exec_order.py
import time


# 多个装饰器的执行顺序
# 如果一个函数添加了多个装饰器，
# 在定义阶段，靠近函数的装饰器先执行，远离函数的装饰器后执行
# 在执行阶段，远离函数的装饰器先执行，靠近函数的装饰器后执行

# 装饰器应用顺序：
        # 离函数近的先包裹
# 执行顺序：
        # 外层先执行，内层后执行

def mylog(func):
    '''日志打印装饰器'''
    print('mylog start')
    def log_inner(*args, **kwargs):
        print('log_inner start')
        func(*args, **kwargs)
        print('log_inner end')
    print('mylog end')
    return log_inner

def cost_time(func):
    '''函数执行时间统计装饰器'''
    print('cost_time start')
    def cost_inner(*args, **kwargs):
        print('cost_inner start')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行耗时：{end-start}秒")
        print('cost_inner end')
    print('cost_time end')
    return cost_inner


# 等价于 fun1 = mylog(cost_time(fun1))
@mylog # 远离函数fun1的装饰器
@cost_time # 靠近函数fun1的装饰器
def fun1(a, b):
    print('fun1 start')
    time.sleep(3)
    print('fun1 end')

# 调用函数，观察日志打印顺序
fun1(10, 2)
'''
日志打印如下：
cost_time start
cost_time end
mylog start
mylog end
log_inner start
cost_inner start
fun1 start
fun1 end
fun1 执行耗时：3.001056432723999秒
cost_inner end
log_inner end
'''