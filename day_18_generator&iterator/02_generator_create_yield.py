#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/24 18:30
# @Author  : George
# @File    : 02_generator_create_yield.py

# yield方式创建生成器

"""
1. 函数有了yield之后，调用它，就会生成一个生成器
2. yield作用：程序挂起，返回相应的值。下次从下一个语句开始执行。
3. return在生成器中代表生成器的值，直接报错：StopIeratation
4. next方法作用：唤醒并继续执行
"""

def test():
    print("start")
    i = 0
    while i<3:
        # yield i
        temp = yield i
        print(f"temp:{temp}")
        print(f"i:{i}")
        i+=1
    print("end")
    return "done"

if __name__ == '__main__':
    a = test() # 实例化方法，创建一个生成器
    print(a) # 打印生成器：<generator object test at 0x000001C5C5A7F850>
    a.__next__() # 第一次执行 a.__next__() ， 执行：print("start")，程序暂停在 yield i， 此时temp是 None, i 是0
    a.__next__() # 第二次执行 a.__next__() ， 程序从 temp = 开始往下执行，i+=1 后继续下一个while循环，然后暂停在 yield i， 此时temp是 None, i 是1，此时还没有执行 print(f"temp:{temp}")
    a.__next__() # 第三次执行 a.__next__() ， 程序从 temp = 开始往下执行，i+=1 后继续下一个while循环，然后暂停在 yield i， 此时temp是 None, i 是2，此时还没有执行 print(f"temp:{temp}")
    a.__next__() # 第四次执行 a.__next__() ， 程序从 temp = 开始往下执行，temp:None，i:2, end, 无法进入while循环了，return “done”，此时会报错：StopIteration: