#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 9:31
# @Author  : George
# @File    : 01_flask_hello.py

from flask import Flask

'''
第一个Flask应用
Flask Hello World
'''

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'hello world'

if __name__ == '__main__':
    # host='0.0.0.0' 表示监听所有地址
    # port=8080 表示监听8080端口
    # debug=True 表示开启调试模式,当代码修改后,服务器会自动重启
    # use_reloader=False 表示不自动重启服务器
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)