# for 循环 else 语句

# 什么情况下会进入 else，就是 for 循环正常的完成遍历，在遍历过程中，没有被打断
# （解释：比如没有执行到 break 语句）。

nums = [1, 2, 3]
for item in nums:
    if item >= 2:
        print(f"当前数字是：{item}")
        break
    else:
        print(f"当前数字是：{item}")
else:
    print("for循环没有被打断，且执行结束了")

