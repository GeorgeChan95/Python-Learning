#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 17:00
# @Author  : George
# @File    : 14_return_tuple.py

'''
返回元组
返回分别是：
    - 响应内容
    - 响应状态码
    - 响应头信息
'''

from flask import Flask

app = Flask(__name__)
@app.route('/tuple/')
def return_tuple():
    # data 是设置的浏览器响应的请求头
    data = {
        'name': 'george',
        'age': 18
    }
    # 666 是设置的响应状态码
    return 'hello', 666, data

if __name__ == '__main__':
    app.run(debug=True, use_reloader = False)