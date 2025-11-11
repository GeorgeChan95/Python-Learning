# 运算符优先级

x = 5
print(x) # 5 正号（通常无实际效果）
print(+x) # 5
print(-x) # -5, 负号（取相反数）
print(~x) # -6, 按位取反

x = -6
print(+x) # -6, 正号（通常无实际效果）

p = 9
q = 4
print(p / q) # 2.25, 除法（浮点数）
print(p // q) # 2, 除法（整数）,向下取整
print(p % q) # 1, 取模（取余）

print(8 << 2) # 32, 左移运算符, 相当于乘以2的n次方, 8 << 2 = 8 * 2^2 = 32
print(8 >> 2) # 2, 右移运算符, 相当于除以2的n次方, 8 >> 2 = 8 / 2^2 = 2

print(5 & 3) # 1, 按位与运算符, 对应位都是1才为1, 0101 & 0011 = 0001 = 1

print(5 ^ 3) # 6, 按位异或运算符, 对应位不同才为1, 0101 ^ 0011 = 0110 = 6

print(5 | 3) # 7, 按位或运算符, 对应位有一个1就为1, 0101 | 0011 = 0111 = 7

print(5 < 10) # True, 小于运算符

str1 = "hello"
str2 = "hello"
print(str1 == str2) # True, 等于运算符, 比较字符串是否相等
print(2 == 2) # True, 等于运算符, 比较数值是否相等

list1 = [1, 2, 3, 4, 5]
a = 1
print(a in list1) # True, 成员运算符, 检查元素是否在列表中
print(6 in list1) # False, 成员运算符, 检查元素是否在列表中

str3 = "world"
print(str1 is str2) # True, 身份运算符, 检查两个变量是否引用同一个对象
print(str1 is not str3) # True, 身份运算符, 检查两个变量是否引用不同的对象

print(not str1 is  str2) # False, not 对布尔值取反

x = 8
y = 2
x <<= 2
print(x) # 32, 左移运算符, 相当于乘以2的n次方, 8 << 2 = 8 * 2^2 = 32

print(x if x > y else y) # 32, 条件运算符, 如果条件为True, 则返回x, 否则返回y
