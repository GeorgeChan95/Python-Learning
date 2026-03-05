#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 18:33
# @Author  : George
# @File    : 01_str_format.py

# 字符串格式化

#旧版本
name = '张三'
age = 20
print('姓名：%s, 年龄：%d', name, age)
print('姓名：{}, 年龄：{}'.format(name, age))

# 新版本
print(f"姓名：{name}, 年龄：{age}")
names = ['George', "Jack"]
print(f"姓名1：{names[0]}, 姓名2:{names[1]}")

# 表达式
a = 10
b = 20
print(f'a和b的和：{a + b}')

# 变量使用=直接赋值,显示 = 号
print(f'{a=}, {b=}') # a=10, b=20


#使用指定的字符填充
name = 'baizhan'
# 20  使用*居中显示
# ^：表示居中对齐
# 20：指定总宽度为20个字符
# *：指定用星号填充空白位置
print("{:*^20}".format(name))
#居右显示
print(f'{name:*>20}')
#居左显示
print(f'{name:*<20}')

#对数值变量的格式化
price = 12.345
print('{:.2f}'.format(price))
print(f'{price:.2f}')

# 显示百分比
pct = 0.789
print('{:.1f}%'.format(pct*100)) # 78.9%
print(f"{pct*100:.1f}%")
