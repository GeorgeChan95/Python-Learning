#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 11:25
# @Author  : George
# @File    : 14_os_path.py

# os模块的应用,操作文件和目录的路径
import os.path

#################获得目录、文件基本信息######################
print(os.path.isabs("d:/a.txt")) #是否绝对路径 True
print(os.path.isdir("d:/a.txt")) #是否目录 False
print(os.path.isfile("d:/a.txt")) #是否文件 True
print(os.path.exists("d:/a.txt")) #文件是否存在 True
print(os.path.getsize("d:/a.txt")) #文件大小 44
print(os.path.abspath("d:/a.txt")) #输出绝对路径 d:\a.txt
print(os.path.dirname("d:/a.txt")) #输出所在目录  d:/


########获得创建时间、访问时间、最后修改时间##########
print(os.path.getctime("a.txt")) #返回创建时间
print(os.path.getatime("a.txt")) #返回最后访问时间
print(os.path.getmtime("a.txt")) #返回最后修改时间

################对路径进行分割、连接操作####################
path = os.path.abspath("a.txt") #返回绝对路径
print(os.path.split(path)) #返回元组：目录、文件 ('E:\\study\\PythonLearning\\Python-Learning\\day11', 'a.txt')

print(os.path.splitext(path)) #返回元组：路径、扩展名 ('E:\\study\\PythonLearning\\Python-Learning\\day11\\a', '.txt')

print(os.path.join("aa","bb","cc")) #返回路径：aa/bb/cc

# 列出指定目录下所有的 .py 文件，并输出文件名
# 获取当前目录下，所有 .py 文件
c_path = os.getcwd() # 当前所在目录：E:\study\PythonLearning\Python-Learning\day11
print(f"当前所在目录：{c_path}")
files = os.listdir(c_path)
for filename in files:
    if filename.endswith(".py"):
        print(filename)
