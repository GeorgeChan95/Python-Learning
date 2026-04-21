#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 16:12
# @Author  : George
# @File    : 11_url_for.py

'''
url_for()函数用于生成URL，它接受函数名作为第一个参数，然后接受关键字参数，每个关键字参数对应URL中的变量部分。
'''

from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/list/<page>/')
def list(page):
    # 获取到请求参数
    num = request.args.get('num')
    # 路径参数
    print(f'路径参数：{page}, 请求参数：{num}')
    return 'list'

'''
访问：http://127.0.0.1:8080/findList
返回：/list/2?num=10
'''
@app.route('/findList/')
def findList():
    # 生成 url
    # 第一个参数是函数方法名，
    # 第二个参数是路径参数
    # 第三个参数是查询参数
    url = url_for('list', page=2, num=10)
    return url

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)