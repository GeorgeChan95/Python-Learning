#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/22 10:33
# @Author  : George
# @File    : 24_template_custome_filter_time.py

'''
自定义时间过滤器
time距离现在的时间间隔
    1. 如果时间间隔小于1分钟以内，那么就显示“刚刚”
    2. 如果是大于1分钟小于1小时，那么就显示“xx分钟前”
    3. 如果是大于1小时小于24小时，那么就显示“xx小时前”
    4. 如果是大于24小时小于30天以内，那么就显示“xx天前”
    5. 否则就是显示具体的时间 2030/10/2016:15
'''

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.template_filter('timeFormat')
def timeFormat(time):
    '''
    自定义时间格式化过滤器
    :param time:
    :return:
    '''
    # 当前时间
    now = datetime.now()
    seconds = (now - time).total_seconds()

    if seconds < 60:
        return '刚刚'
    elif seconds < 60 * 60:
        minutes = int(seconds/60)
        return f'{minutes}分钟前'
    elif seconds < 60 * 60 * 24:
        hour = int(seconds / (60*60))
        return f'{hour}小时前'
    elif seconds < 60 * 60 * 24 * 30:
        day = int(seconds / (60 * 60 * 24))
        return f'{day}天前'
    else:
        return '很久以前'

@app.route('/')
def index():
    time = datetime(2026, 4, 22, 8, 0, 0)
    seconds = (datetime.now() - time).total_seconds()
    return render_template('24_template_custome_filter_time.html', send_time = time, seconds = seconds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader = False)



