print("我有{}元".format(100.5))
# 我有100.5元

print("{}, {}".format("Hello", "Python"))
# Hello, Python

print("{0}, {1}".format("Hello", "World"))
# Hello, World

print("{1}, {0}, {1}".format("Hello", "World"))
# World, Hello, World

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 网站名：菜鸟教程, 地址 www.runoob.com

my_list = ["Hello", "Python"]
my_list2 = ["你好", "乔治"]
print("元素1：{0[0]}, 元素2：{0[1]}".format(my_list, my_list2))
print("元素1：{1[0]}, 元素2：{1[1]}".format(my_list, my_list2))
# 元素1：Hello, 元素2：Python
# 元素1：你好, 元素2：乔治