#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 20:17
# @Author  : George
# @File    : 22_template_filter_other.py
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('22_template_filter_other.html')

if __name__ =='__main__':
    app.run(debug=True, use_reloader=False)