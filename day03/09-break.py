# break 的使用
import random

count = 0
while count < 100:
    count += 1
    a = random.randint(1, 100)
    if a == 10:
        break
    print("count的值是：", count)
else:
    print("while 运行结束，没有中断")


print('---------------------------------')


# . 1 - 100 以内的求和，求出当和第一次大于 20 的当前控制循环的变量是多少
sum = 0
for i in range(1, 100+1):
    sum += i
    if sum > 20:
        break
print(f"sum = {sum}，此时i的值是：{i}")