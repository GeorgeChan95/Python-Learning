#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/13 10:14
# @Author  : George
# @File    : 02_file_read.py

file = open("D://aaa//hello.txt", "r", encoding="UTF-8")

# # 读取方式1: f.read(), read()方法默认读取文件全部内容，包含换行符
#                       read(6) 读取指定的长度
# 读取文件的全部内容
content_all = file.read()
print(f"读取到hello.txt内容如下：\n{content_all}")

# 读取指定长度的内容
file.seek(0) # 将读取指针重新定位到文件的开头
content_part = file.read(6)
print(f"读取到hello.txt内容如下：\n{content_part}")


# # 读取方式2: f.readline(), 注意readline, 字符串末尾保留换行符\n
file.seek(0) # 将读取指针重新定位到文件的开头
line1 = file.readline()
line2 = file.readline()
print(f"第一行内容：{line1}")
print(f"第二行内容：{line2}")


# # 读取方式3: f.readlines()列表形式读取文件中的所有行
# 一次性读取全部内容（不包含读取指针前面的内容）
print("--------------- readlines()读取全部内容 ---------------")
file.seek(0)
line_all = file.readlines()
for line in line_all:
    print(f"文本内容：{line}", end="")


# 读取方式4: for line in file 形式读取文件
print("\n--------------- for line in file 形式读取文件 ---------------")
file.seek(0)
for line in file:
    print(f"文本内容：{line}", end="")


# 关闭文件流（文件的读和写在操作完成后，都需要关闭文件流，避免内存的泄露）
file.close()