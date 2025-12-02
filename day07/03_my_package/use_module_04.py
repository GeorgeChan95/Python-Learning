#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/2 19:51
# @Author  : George
# @File    : use_module_04.py


print("---------------------- 方式四 ----------------------")
from other_package import *

# other_package 在 __init__.py 配置了 __all__ = ['test2']，
# 因此这里不能调用  test_module.kk()

# test_module.kk()
test2.cc()