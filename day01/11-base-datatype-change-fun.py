# 内置函数对数据进行显示类型转换

#### 1.int(x [, base])
# 将浮点数转换为整数（向下取整）
print(int(3.9))          # 输出: 3

# 将字符串转换为整数
print(int("25"))          # 输出: 25

# 将二进制字符串转换为整数（指定 base=2,即二进制）
print(int("1010", 2))     # 输出: 10
print(int("11", 8))     # 输出: 10

print("#################### float(x) —— 转换为浮点数 ####################")

#### 2.float(x) —— 转换为浮点数
# 整数转浮点
print(float(5))           # 输出: 5.0

# 字符串转浮点
print(float("3.14"))      # 输出: 3.14

# 科学计数法
print(float("1e-3"))      # 输出: 0.001


print("#################### complex(real [, imag]) —— 创建复数 ####################")
# 3. complex(real [, imag]) —— 创建复数
# 传入实部和虚部
print(complex(2, 3))      # 输出: (2+3j)

# 仅传实部
print(complex(5))         # 输出: (5+0j)

# 从字符串创建复数
print(complex("4+2j"))    # 输出: (4+2j)

# 复数的计算
a = complex(2, 3)   # 2 + 3j
b = complex(1, -1)  # 1 - 1j

print(a + b)  # 输出: (3+2j)
print(a - b)  # 输出: (1+4j)
print(a * b)  # 输出: (5+1j)
print(a / b)  # 输出: (-0.5+2.5j)


print("#################### str(x) —— 转换为字符串 ####################")
# 4.str(x) —— 转换为字符串
# 数字转字符串
print(str(123))           # 输出: '123'

# 列表转字符串
print(str([1, 2, 3]))     # 输出: '[1, 2, 3]'

# 布尔值转字符串
print(str(True))          # 输出: 'True'


print("#################### repr(x) —— 转换为表达式字符串（可 eval 还原） ####################")
# 5.repr(x) —— 转换为表达式字符串（可 eval 还原）
# 字符串 repr
print(repr("hello"))      # 输出: "'hello'"

# 列表 repr
x = [1, 2, 3]
print(repr(x))    # 输出: '[1, 2, 3]'

# 可被 eval() 执行还原
s = repr({"a": 1})
print(eval(s))            # 输出: {'a': 1}


print("#################### eval(str) —— 执行字符串表达式并返回结果 ####################")
# 6.eval(str) —— 执行字符串表达式并返回结果
# 简单表达式
print(eval("3 + 5"))      # 输出: 8

# 调用函数
x = 10
print(eval("x * 2"))      # 输出: 20

# 还原对象（和 repr 配合）
obj = eval("{'name': 'Tom', 'age': 20}")
print(obj["name"])        # 输出: Tom


print("#################### tuple(s) —— 序列转元组 ####################")
# 7.tuple(s) —— 序列转元组
# 列表转元组
print(tuple([1, 2, 3]))   # 输出: (1, 2, 3)

# 字符串转元组（按字符拆分）
print(tuple("abc"))       # 输出: ('a', 'b', 'c')

# 集合转元组
print(tuple({5, 6, 7}))   # 输出: (5, 6, 7)
print(tuple({5, 6, 7})[0])   # 输出: 5



print("#################### list(s) —— 序列转列表 ####################")
# 8.list(s) —— 序列转列表
# 元组转列表
print(list((1, 2, 3)))    # 输出: [1, 2, 3]

# 字符串转列表（拆分成字符）
print(list("hi"))         # 输出: ['h', 'i']

# 集合转列表
print(list({9, 8, 7}))    # 输出: [8, 9, 7]（集合无序）


print("#################### set(s) —— 转换为可变集合 ####################")
# 9.set(s) —— 转换为可变集合
# 列表转集合（去重）
print(set([1, 2, 2, 3]))  # 输出: {1, 2, 3}

# 字符串转集合
print(set("hello"))       # 输出: {'h', 'e', 'l', 'o'}
print(set({"hello", "python"}))       # 输出: {'python', 'hello'}

# 元组转集合
print(set((1, 2, 3)))     # 输出: {1, 2, 3}


print("#################### dict(d) —— 创建字典 ####################")
# 10.dict(d) —— 创建字典
# 从 key-value 元组序列创建
print(dict([("a", 1), ("b", 2)]))   # 输出: {'a': 1, 'b': 2}

# 从关键字参数创建
qq = dict(name="Tom", age=20)
print(qq)     # 输出: {'name': 'Tom', 'age': 20}
print(qq.get("name")) # 输出: Tom

# 使用 zip() 组合
print(dict(zip(["x", "y"], [1, 2]))) # 输出: {'x': 1, 'y': 2}


print("#################### frozenset(s) —— 创建不可变集合 ####################")
# 11.frozenset(s) —— 创建不可变集合
# 创建不可变集合
fs = frozenset([1, 2, 3])
print(fs)                   # 输出: frozenset({1, 2, 3})

# 可用于字典键（set 不行）
d = {fs: "immutable"}
print(d)                    # 输出: {frozenset({1, 2, 3}): 'immutable'}

# frozenset 也可去重
print(frozenset("hello"))   # 输出: frozenset({'h', 'e', 'l', 'o'})

fs = frozenset({1, 2, 3})

# 循环打印每个元素
for elem in fs:
    print(elem)

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})

print(a | b)  # 并集 → frozenset({1, 2, 3, 4, 5})
print(a & b)  # 交集 → frozenset({3})
print(a - b)  # 差集 → frozenset({1, 2})

print("#################### chr(x) —— 将整数转为字符 ####################")
# 12.chr(x) —— 将整数转为字符
# ASCII 编码转字符
print(chr(65))             # 输出: 'A'

# Unicode 编码转字符
print(chr(20013))          # 输出: '中'

# 常见示例
print(chr(48))             # 输出: '0'
