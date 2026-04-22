#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/22 14:33
# @Author  : George
# @File    : 27_template_for_1.py

'''
模板循环控制结构
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    items = ['apple', 'banana', 'orange', 'pear', 'grape', 'watermelon']
    person = {
        'name' : 'George',
        'age' : 18,
        'gender' : 'male',
        'height' : 1.88,
        'weight' : 75
    }
    return render_template('27_template_for_1.html', items = items, person = person)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)