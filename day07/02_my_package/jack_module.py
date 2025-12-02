#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/2 18:49
# @Author  : George
# @File    : jack_module.py

# 其它模块导入该模块时，如果使用的是 from 模块名 import * 的形式，则只会导入 ok() 函数
__all__=['ok']

def hi():
    print("jack say hi")

def ok():
    print("jack say ok")

print(__name__) #

# 仅当运行该文件时，运行函数 hi()
if __name__ == "__main__" :
    hi()


