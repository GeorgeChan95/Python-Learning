#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 18:48
# @Author  : George
# @File    : 17_template_params.py

'''
模板传参
'''

from flask import Flask, render_template
app = Flask(__name__)

'''
单个参数的传递，直接  参数名 = 参数值 形式传递
'''
@app.route('/index1/')
def index1():
    name = '张三'
    age = 18
    return render_template('17_template_params.html', name = name, age = age)


@app.route("/index2/")
def index2():
    context = {
        'name': '李四',
        'age': 20,
        'family': { 'father': '李华', 'mother': '王丽'}
    }

    # **context 的作用是：把字典拆开，变成一个个“键=值”的参数传进去
    return render_template('17_template_params.html', **context)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

