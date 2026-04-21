#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 18:37
# @Author  : George
# @File    : 16_use_template.py

'''
学习模板的使用
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('16_use_template.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)