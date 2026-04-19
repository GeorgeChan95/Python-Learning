#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 13:52
# @Author  : George
# @File    : 04_url_custom_convert.py

'''
1. 自定义转换器
'''
from werkzeug.routing import BaseConverter
from flask import Flask


class PhoneConverter(BaseConverter):
    regex = '1[3-9]\d{9}'

app = Flask(__name__)

app.url_map.converters['phone'] = PhoneConverter

@app.route('/user/<phone:number>') # /user/13890908978
def phone(number):
    print(f'手机号为：{number}')
    return f"用户手机号为：{number}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

