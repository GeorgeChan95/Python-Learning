#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/2 20:06
# @Author  : George
# @File    : 09_alternation_operator.py

# 择一匹配符的使用
# search方法搜索一个字符串，要想搜索多个字符串，如搜索aa、bb
# 和cc，最简单的方法是在文本模式字符串中使用择一匹配符号
# （|)。择一匹配符号和逻辑或类似，只要满足任何一个，就算匹配成功。

import re

pattern = 'aa|bb|cc'
str = 'aa' # <re.Match object; span=(0, 2), match='aa'>
str = 'ab' # None
str = 'bb' # <re.Match object; span=(0, 2), match='bb'>
str = 'cc' # <re.Match object; span=(0, 2), match='cc'>
str = 'aa|bb' #  <re.Match object; span=(0, 2), match='aa'>
# print(re.match(pattern, str))


# 匹配0-100之间所有的数字
pattern = r'[1-9]?\d$|100$'
str = '0' # <re.Match object; span=(0, 1), match='0'>
str = '1' # <re.Match object; span=(0, 1), match='1'>
str = '10' # <re.Match object; span=(0, 2), match='10'>
str = '99' # <re.Match object; span=(0, 2), match='99'>
str = '100' # <re.Match object; span=(0, 3), match='100'>
str = '101' # None
# print(re.match(pattern, str))


# '[xyz]' 和 'x|y|z'
pattern = '[xyz]'
pattern1 = 'x|y|z'
print(re.match(pattern,'y')) # <re.Match object; span=(0, 1), match='y'>
print(re.match(pattern1,'y')) # <re.Match object; span=(0, 1), match='y'>