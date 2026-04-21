#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 19:44
# @Author  : George
# @File    : 19_template_filter_1.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('19_template_filter_1.html', num = -20)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)