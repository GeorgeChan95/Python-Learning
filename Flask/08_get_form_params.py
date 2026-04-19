#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 15:14
# @Author  : George
# @File    : 08_get_form_params.py

'''
获取表单参数
POST 请求携带 form表单数据
url: localhost:5000/login
    method: POST
    data: username=George
        password=123456

返回：username: George, password: 123456
'''
import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])  # methods参数指定请求方法，默认为GET
def login():
    username = request.form.get("username")
    password = request.values.get("password")
    return f"username: {username}, password: {password}"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
