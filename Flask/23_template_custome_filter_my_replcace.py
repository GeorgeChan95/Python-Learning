#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/22 10:12
# @Author  : George
# @File    : 23_template_custome_filter_my_replcace.py
'''
自定义内容过滤器
'''

from flask import Flask, render_template
app = Flask(__name__)

'''
自定义过滤器 my_replcace
将模板文本内容，替换成指定的文本
'''
@app.template_filter('my_replcace')
def my_replcace(value, arg, replaceStr): # value是传入的值，arg是传入的参数, replaceStr是替换的值
    return value.replace(arg, replaceStr)

@app.route('/') # 路由
def inde():
    return render_template('23_template_custome_filter_my_replcace.html', text='hello world')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)