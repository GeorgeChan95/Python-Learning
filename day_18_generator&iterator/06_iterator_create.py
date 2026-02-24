#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/2/24 19:28
# @Author  : George
# @File    : 06_iterator_create.py

# 自定义一个迭代器
# 重点，需要重写 __iter__ 方法 和  __next__ 方法

class MyNumbers:
    def __iter__(self):
        self.num = 10
        return self

    def __next__(self):
        if self.num < 50:
            i = self.num + 10
            self.num = i
            return i
        else:
            return StopIteration

myClass = MyNumbers()
iterClass = iter(myClass)

print(iterClass.__next__()) # 20
print(iterClass.__next__()) # 30
print(iterClass.__next__()) # 40
print(iterClass.__next__()) # 50
print(iterClass.__next__()) # <class 'StopIteration'>