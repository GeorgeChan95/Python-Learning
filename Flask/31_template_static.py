#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/23 20:05
# @Author  : George
# @File    : 31_template_static.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("31_template_static.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)