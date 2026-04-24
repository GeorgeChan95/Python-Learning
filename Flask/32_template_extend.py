#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/24 8:47
# @Author  : George
# @File    : 32_template_extend.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("32_template_extend.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)