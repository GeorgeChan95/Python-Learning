#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 19:56
# @Author  : George
# @File    : 20_template_filter_default.py

'''
默认值过滤器的使用
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("20_template_filter_default.html", nick_name = None)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)