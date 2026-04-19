#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 14:28
# @Author  : George
# @File    : 06_to_url_test.py

'''
to_url 测试
1、访问 /show_url ，返回：/show_params/GEORGE/18
2、访问 /show_params/GEORGE/18 ，返回：获取到用户名：GEORGE, 年龄：18
'''
import typing as t

from flask import Flask, url_for
from werkzeug.routing import BaseConverter

class UrlForConverter(BaseConverter):

    def to_python(self, value: str):
        print('to_python函数被调用')
        return value.upper()

    def to_url(self, value):
        print('to_url 函数被调用')
        if isinstance(value, str):
            return value.upper()
        if isinstance(value, int):
            return str(value)

app = Flask(__name__)

app.url_map.converters['url'] = UrlForConverter

@app.route('/show_params/<url:name>/<url:age>')
def show_params(name: str, age: int):
    print(f"获取到用户名：{name}, 年龄：{age}")
    return f"获取到用户名：{name}, 年龄：{age}"

@app.route('/show_url')
def show_url():
    link = url_for('show_params', name='George', age=18)
    return link

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)