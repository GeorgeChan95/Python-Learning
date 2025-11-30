#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/30 12:11
# @Author  : George
# @File    : 21-dict_create.py

books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
dict_book = {book: author for book, author in zip(books, authors)}
print("dict_book:", dict_book)  # dict_book: {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '西游记': '吴承恩', '水浒传': '施耐庵'}



str1 = "孙悟空"
dict_str = {ele1: ele2 * 2 for ele1, ele2 in zip(str1, str1)}
print("dict_str:", dict_str) # dict_str: {'孙': '孙孙', '悟': '悟悟', '空': '空空'}