# 打印空心金字塔
# 总层数
total_level = 10

# i 控制层数
for i in range(1, total_level + 1): # i 从1开始，直到5
    # k 控制输出空格数
    for k in range(total_level - i): # k 从0开始，最大是3
        print(" ", end="")
        # j 控制每层输出的*号个数
    for j in range(2 * i - 1): # j 从0开始
        if j == 0 or j == 2 * i - 2 or i == total_level:
            print("*", end="")
        else:
            print(" ", end="")
        # 每层输出后，换行
    print("")