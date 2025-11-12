# for 循环
import random

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(f"当前数字是：{num}")

print("--------------------------")

list1 = range(1, 10) # 生成一个从1到10的整数序列, 不包含10
list2 = range(1, 10, 2) # 生成一个从1到10的整数序列，步长为2, 不包含10
# list3 = range(0.1, 10, 0.5) # range() 函数不支持浮点数序列
print(list1)
for item in list2:
    print(f"当前浮点数是：{item}")

random.random() # 生成一个0到1之间的随机浮点数
list3 = [random.random() for i in range(10)] # 循环调用 random.random() 得到一个浮点数，然后把它追加到 list3 中
for item2 in list3:
    print(f"当前随机浮点数是：{item2}")

print("--------------------------")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print("--------------------------")