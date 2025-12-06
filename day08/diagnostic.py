#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 15:52
# @Author  : George
# @File    : diagnostic.py
# diagnostic.py
import sys

print("=" * 50)
print(f"Python 版本: {sys.version}")
print(f"sys.version_info: {sys.version_info}")
print("=" * 50)

# 1. 检查 tuple 类型
print("\n1. 检查 tuple 类型:")
print(f"   type(tuple) = {type(tuple)}")
print(f"   tuple.__name__ = {tuple.__name__}")

# 2. 检查是否有局部变量覆盖
print("\n2. 检查局部变量:")
if 'tuple' in locals():
    print(f"   ⚠️ 警告: 局部变量 'tuple' 存在，值为: {locals()['tuple']}")
else:
    print("   ✅ 局部变量中没有 'tuple'")

if 'tuple' in globals():
    val = globals()['tuple']
    if val is not __builtins__.tuple:
        print(f"   ⚠️ 警告: 全局变量 'tuple' 被覆盖，值为: {val}")
        print(f"   类型: {type(val)}")
    else:
        print("   ✅ 全局变量 'tuple' 是内置类型")
else:
    print("   ✅ 全局变量中没有自定义的 'tuple'")

# 3. 尝试最简单的类型注解
print("\n3. 测试最简单的类型注解:")
try:
    test_var: str = "hello"
    print(f"   ✅ 简单类型注解成功: {test_var}")
except Exception as e:
    print(f"   ❌ 失败: {e}")

# 4. 测试元组类型注解
print("\n4. 测试元组类型注解:")
try:
    my_tuple: tuple[str, str, str, float] = ("run", "sing", "fly", 1.1)
    print(f"   ✅ 元组类型注解成功: {my_tuple}")
except TypeError as e:
    print(f"   ❌ 失败: {e}")
    print(f"   错误类型: {type(e).__name__}")
    import traceback
    print(f"   完整错误追踪:")
    traceback.print_exc()

# 5. 测试不使用类型注解
print("\n5. 测试不使用类型注解:")
try:
    my_tuple2 = ("run", "sing", "fly", 1.1)
    print(f"   ✅ 创建元组成功: {my_tuple2}")
    print(f"   类型: {type(my_tuple2)}")
except Exception as e:
    print(f"   ❌ 失败: {e}")

# 6. 测试其他类型注解
print("\n6. 测试其他类型注解:")
try:
    my_list: list[int] = [1, 2, 3]
    print(f"   ✅ 列表类型注解成功: {my_list}")
except Exception as e:
    print(f"   ❌ 失败: {e}")

print("\n" + "=" * 50)
print("诊断完成")
print("=" * 50)