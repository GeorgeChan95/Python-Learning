#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/22 14:06
# @Author  : George
# @File    : 26_template_ifelse_2.py

'''
模板分支流程练习
'''

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('26_template_ifelse_2.html')

@app.route('/login/')
def login():
    user = request.args.get('user')
    return render_template('26_template_ifelse_2.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader = False)