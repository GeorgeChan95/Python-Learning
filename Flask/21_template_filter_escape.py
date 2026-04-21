#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 19:56
# @Author  : George
# @File    : 21_template_filter_escape.py

'''
转移字符过滤器的使用
如果开启了全局转义，那么safe过滤器会将变量关掉转义
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    info = '<script>alert("Hello!!")</script>'
    return render_template("21_template_filter_safe.html", info = info)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)