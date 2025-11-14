# return 的使用

# 定义函数
def testReturnFun():
    for j in range(20, 30):
        print(f"*****当前j的值是：{j}")
        for i in range(1, 5):
            if i == 3:
                return # return 也会同时退出外层循环
            print(f"当前i的值是：{i}")

testReturnFun()

# 打印结果如下：
"""
*****当前j的值是：20
当前i的值是：1
当前i的值是：2
"""