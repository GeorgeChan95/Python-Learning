#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/20 10:58
# @Author  : George
# @File    : 12_os_app.py

# os模块的应用,打开电脑上的app
import os

# os.startfile(path) 是 Windows 系统特有的函数，用于通过文件关联打开指定路径的文件/应用程序。
# 路径 C://Program Files//Google//Chrome//Application//chrome.exe 是 Chrome 浏览器可执行文件的默认安装路径（// 是 Python 字符串中转义后的路径分隔符，等效于 Windows 中的 \）。
# 注意：若用户 Chrome 浏览器安装路径非默认（如自定义安装到其他盘或目录），此行代码会因路径错误而执行失败。
# os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")

# os.system(command) 用于在系统 shell 中执行命令。
# notepad.exe 是 Windows 系统自带的记事本应用程序，由于其路径已添加到系统环境变量，因此无需指定完整路径，直接执行命令即可启动。
# os.system("notepad.exe")

# 设置控制台代码页为UTF-8（65001为UTF-8编码的代码页编号）
# os.system("chcp 65001")
os.system("ping www.baidu.com")
