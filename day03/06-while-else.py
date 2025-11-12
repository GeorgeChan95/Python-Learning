# while 循环 else 语句

i = 1
while i < 3:
    print(f"当前数字是：{i}")
    i += 1
    # if i == 2: # 测试 break 中断wihle 执行。
    if i == 4:
        print("while循环被打断了")
        break
else:
    print("while循环没有被打断，且执行结束了")
    print("i < 3 不成立，i 的值是：", i)
