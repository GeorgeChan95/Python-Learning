#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/22 17:24
# @Author  : George
# @File    : 28_template_macro.py
'''
模板宏的使用
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('28_template_macro.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)