#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/23 19:41
# @Author  : George
# @File    : 30_template_set_with.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('30_template_set_with.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)