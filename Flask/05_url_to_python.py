#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 14:13
# @Author  : George
# @File    : 05_url_to_python.py
import typing as t

from flask import Flask
from  werkzeug.routing import BaseConverter

'''
to_python 方法：将url中的参数转为python对象
'''

app = Flask(__name__)

class UpperConverter(BaseConverter):
    def to_python(self, value):
        print("to_python 被调用:", value)
        # 将url中的参数转为大写
        return value.upper()

# 将自定义的转换器注册到app中
app.url_map.converters['upper'] = UpperConverter

'''
请求：/user/abc
响应：Hello, ABC
自动调用了 UpperConverter.to_python 方法
'''
@app.route('/user/<upper:user_name>')
def user(user_name):
    return f'Hello, {user_name}'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
