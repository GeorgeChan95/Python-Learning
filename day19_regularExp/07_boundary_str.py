#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/2 19:18
# @Author  : George
# @File    : 07_boundary_str.py

# 边界字符的使用
import re

r'''
^   匹配字符串开头
$   匹配字符串结尾
\b  匹配一个单词的边界
\B  匹配非单词的边界
'''

# ^ 匹配字符串开头
# 匹配 hello 开头的字符串， .* 表示任意字符任意次数
pattern = '^hello.*'
str = 'hello world' # <re.Match object; span=(0, 11), match='hello world'>
str = 'h ww' # None
str = '1hello wor' # None
str = 'hello你好' # <re.Match object; span=(0, 7), match='hello你好'>
str = 'hellopython' # <re.Match object; span=(0, 11), match='hellopython'>
# print(re.match(pattern, str))

pattern = '^hello'
str = "Hello world"
# 忽略大小写
# print(re.match(pattern, str, re.I)) # <re.Match object; span=(0, 5), match='Hello'>


# $ 匹配字符串结尾
# 匹配一个{5,10}位的qq邮箱
pattern = r'[1-9]\d{4,9}@qq.com$'
str = '12345@qq.com' # <re.Match object; span=(0, 12), match='12345@qq.com'>
str = 'A2345@qq.com' # None
str = '3h333998@qq.com' # None
str = '1234567899000@qq.com' # None
# print(re.match(pattern, str))


# \b 匹配一个单词的边界
# 左边界
pattern = r'.*\bqwe'
str = 'abc qwe' # <re.Match object; span=(0, 7), match='abc qwe'>
str = 'abc_qwe' # None
str = 'abcqwe' # None
str = 'abc.qwe' # <re.Match object; span=(0, 7), match='abc.qwe'>
str = 'abc qwe ' # <re.Match object; span=(0, 7), match='abc qwe'>
str = 'abc qwe vvv' # <re.Match object; span=(0, 7), match='abc qwe'>
str = 'abc qwea' # <re.Match object; span=(0, 7), match='abc qwe'>
# print(re.match(pattern, str))

# 右边界
pattern = r'qwe\b.*'
str = 'qwe abc' # <re.Match object; span=(0, 7), match='qwe abc'>
str = 'qwe.abc' # <re.Match object; span=(0, 7), match='qwe.abc'>
str = 'ttt qwe abc' # None (换成search就不是None了)
str = 'qwe_abc' # None
# print(re.match(pattern, str))


# \B 匹配非单词的边界
# 左边界
pattern = r'.*\Bqwe'
str = 'abc qwe' # None
str = 'abc_qwe' # <re.Match object; span=(0, 7), match='abc_qwe'>
str = 'abcqwe' # <re.Match object; span=(0, 6), match='abcqwe'>
str = 'abc.qwe' # None
# str = 'abc qwe ' # None
str = 'abc qwe vvv' # None
str = 'abc qwea' # None
# print(re.match(pattern, str))

# 右边界
pattern = r'qwe\B.*'
str = 'qwe abc' # None
str = 'qwe.abc' # None
str = 'ttt qwe abc' # None
str = 'qwe_abc' # <re.Match object; span=(0, 7), match='qwe_abc'>
print(re.match(pattern, str))