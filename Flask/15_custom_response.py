#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 17:09
# @Author  : George
# @File    : 15_custom_response.py

from flask import Flask, Response, make_response
app = Flask(__name__)

'''
创建 Response
'''
@app.route('/')
def index():
    return Response('你好，少年！！',status=500,headers={'name':'python!!!'})
    # return Response('')
    # return Response('无法找到页面', status=404)


'''
make_response方式
'''
@app.route('/make_response/')
def home():
    # 方式一：直接创建
    resp = make_response('你好，少年！！', 500, {'name':'python!!!'})
    # 方式二：单独设置
    resp.headers['age'] = '30'
    resp.set_cookie('username', 'zhangsan')
    resp.status = 200
    return resp


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)