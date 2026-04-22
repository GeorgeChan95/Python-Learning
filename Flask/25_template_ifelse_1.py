#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/22 11:26
# @Author  : George
# @File    : 25_template_ifelse_1.py
'''
模板流程分支结构
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('25_template_ifelse_1.html', name = 'George', age = 20)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True, use_reloader = False)