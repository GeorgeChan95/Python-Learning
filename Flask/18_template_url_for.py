#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/21 19:13
# @Author  : George
# @File    : 18_template_url_for.py

from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/home/<int:userid>/')
def home(userid):
    return render_template('18_template_url_for.html', userid=userid)


@app.route("/index/<int:userid>/")
def index(userid):
    name = request.args.get('name')
    return f"获取用户id：{userid}, 用户名：{name}"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)