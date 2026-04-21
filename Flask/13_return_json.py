#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 16:55
# @Author  : George
# @File    : 13_return_json.py

'''
Flask 返回 JSON 数据
'''

from flask import Flask, jsonify

app = Flask(__name__)

'''
方式1：使用 jsonify 函数，将字典转成json
'''
@app.route('/json/')
def return_json():
    data = {
        'name': 'George',
        'age': 18,
        'gender': 'male'
    }
    return jsonify(data)

'''
方式2：直接返回字典，Flask会自动将字典转成json
'''
@app.route('/json2/')
def return_json2():
    data = {
        'name': 'George222',
        'age': 182,
        'gender': 'male'
    }
    return data

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)