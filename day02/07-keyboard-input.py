# 键盘输入

name = input("请输入姓名：")
age = input("请输入年龄：")

print(f"姓名：{name}, 年龄：{age}")
print("去年年龄：", int(age) - 1) # 键盘输入的默认都是字符串，需要这里转成 int