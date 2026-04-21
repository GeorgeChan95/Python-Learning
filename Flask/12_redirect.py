#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 16:35
# @Author  : George
# @File    : 12_redirect.py

'''
请求重定向
'''

from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route('/login')
def login():
    name = request.args.get('name')
    pwd = request.args.get('pwd')
    print(f'获取到用户名：{name}, 密码：{pwd}')
    return '登录成功'

@app.route('/home')
def home():
    return '主页'

@app.route('/profile')
def profile():
    # 第一个参数：重定向的地址，由url_for进行了转换
    # 第二个参数：302 永久重定向
    return redirect(url_for('login', name='george', pwd='123456'), code=302)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)