#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 15:49
# @Author  : George
# @File    : 10_cookies_headers.py

'''
Flask 中的 cookies 和 headers获取
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    cookie = request.cookies # 获取 cookie信息
    uid = request.cookies.get('uid')

    # 获取header信息
    user_agent = request.headers.get('User-Agent')
    print(f'获取到cookie：{uid}, user_agent: {user_agent}')
    return 'cookie'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
