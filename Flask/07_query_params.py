#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 15:08
# @Author  : George
# @File    : 07_query_params.py

'''
查看参数获取1
请求：/params?name=George&age=20 ， 响应：获取到查询参数 name：George， age: 20
'''

from flask import Flask, request

app = Flask(__name__)

@app.route('/params')
def get_params():
    # 获取查询参数
    name = request.args.get('name')
    age = request.values.get('age')
    return f'获取到查询参数 name：{name}， age: {age}'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)