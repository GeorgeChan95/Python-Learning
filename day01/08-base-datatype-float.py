import sys
from decimal import Decimal

n3 = 5.12
n4 = .512 # 这也行？
print("n4 = ", n4)

n5 = 5.12e2 # 5.12乘以10的2次方
print("n5 = ", n5)

n6 = 5.12e-2 # 5.12除以10的2次方
print("n6 = ", n6)

# float
print(sys.float_info.max) # 浮点数所能表示的最大正数 1.7976931348623157e+308
print(sys.float_info.min) # 浮点数所能表示的最小正数 2.2250738585072014e-308

# float 计算精度缺失
b = 8.1 / 3;
print(b) # 2.6999999999999997
# 使用 Decimal 解决计算精度缺失的问题
x = Decimal("8.1")
y = Decimal("3")
z = x / y
print("z = ", z) # z =  2.7

#### 错误示例：
o = Decimal(8.1) # 如果不是以字符串形式传入参数，那么在内存中存储的其实不是 8.1 ，而是近似 8.1 的数值，精度已经缺失了。
p = Decimal(3)
q = o / p
print("q = ", q) # q =  2.699999999999999881576210707


