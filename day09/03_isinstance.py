#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/10 19:31
# @Author  : George
# @File    : 03_isinstance.py

class AA:
    pass

class BB(AA):
    pass

class CC:
    pass

aa = AA()
bb = BB()

print(f"bb是BB对象：", isinstance(bb, BB)) # True
print(f"bb是AA对象：", isinstance(bb, AA)) # True
print(f"bb是CC对象：", isinstance(bb, CC)) # False


a = 9 # int类型
print(f"a 是int类型：", isinstance(a, int)) # True
print(f"a 是str类型：", isinstance(a, str)) # False
print(f"a 是在int/str/list类型中：", isinstance(a, (int, str, list))) # True
