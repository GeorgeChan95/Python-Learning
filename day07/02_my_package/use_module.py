#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/2 18:57
# @Author  : George
# @File    : use_module.py

# 方式一，import 模块名
import jack_module
jack_module.hi()
jack_module.ok()

# 方式二：from 模块名 import * ， 这样只能导入 ok 函数，因为，在 jack_module 中 __all__=['ok'] 限制了此种方式只暴露 ok 函数
from jack_module import *

ok()
print(__name__) #