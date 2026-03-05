#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 20:10
# @Author  : George
# @File    : 11_match.py

status = 300
match status:
    case 200:
        print('成功')
    case 300:
        print('重定向')
    case 400:
        print('客户端错误')
    case 500:
        print('服务器错误')
    case _:
        print('未知状态码')


p1 = ('zs',23,'man')
p2 = ('lili',24,'woman')
p3 = ('xiaoqiang',25,'man')
p4 = ('xiaoqiang',25,'male')

def fun_test(person):
    match person:
        case ('zs',_,_): # _ 表示任意值
            print('这是张三')
        case (name, 24,_): # name 表示任意值，24 表示年龄
            print('这是李四')
        case ('xiaoqiang',_,_):
            print('这是小强')
        case _:
            print('未知人物')

fun_test(p1) # 这是张三
fun_test(p2) # 这是李四
fun_test(p4) # 这是小强
