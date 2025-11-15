# list、tuple、set 和 dict 传参机制

# list数据类型，即便内容发生了变化，但是引用地址不会发生变化
def f1(my_list):
    print(f"******my_list的内容：{my_list},\tmy_list的地址：{id(my_list)}")
    my_list[0] = "jack"
    print(f"******my_list的内容：{my_list},\tmy_list的地址：{id(my_list)}")

print("-" * 30 + "list" + "-" * 30) # ------------------------------list------------------------------
my_list = ['hi', 'python', 'world']
print(f"my_list的内容：{my_list},\tmy_list的地址：{id(my_list)}")
f1(my_list)
print(f"my_list的内容：{my_list},\tmy_list的地址：{id(my_list)}")
'''
打印如下：
------------------------------list------------------------------
my_list的内容：['hi', 'python', 'world'],	my_list的地址：1819058753792
******my_list的内容：['hi', 'python', 'world'],	my_list的地址：1819058753792
******my_list的内容：['jack', 'python', 'world'],	my_list的地址：1819058753792
my_list的内容：['jack', 'python', 'world'],	my_list的地址：1819058753792
'''



# 在 Python 中，tuple（元组） 是一种不可变的有序数据类型，用于存储多个元素的集合。
# 与列表（list）类似，元组可以包含不同类型的元素，但一旦创建，其内容（元素或顺序）无法修改。
def f2(my_tuple):
    print(f"-----my_tuple的内容: {my_tuple} 地址：{id(my_tuple)}")

print("-" * 30 + "tuple" + "-" * 30)
my_tuple = ("hi", "ok", 1, 0.5, my_list)
print(f"①my_tuple: {my_tuple} 地址：{id(my_tuple)}")
f2(my_tuple)
print(f"④my_tuple: {my_tuple} 地址：{id(my_tuple)}")
'''
打印如下：
------------------------------tuple------------------------------
①my_tuple: ('hi', 'ok', 1, 0.5, ['jack', 'python', 'world']) 地址：3019052498384
-----my_tuple的内容: ('hi', 'ok', 1, 0.5, ['jack', 'python', 'world']) 地址：3019052498384
④my_tuple: ('hi', 'ok', 1, 0.5, ['jack', 'python', 'world']) 地址：3019052498384
'''


# Set 数据类型是一个无序集合，修改了集合内的元素，引用在内存中的地址不变
def f3(my_set):
    print(f"*****my_set的内容：{my_set},\tmy_set的地址{id(my_set)}")
    my_set.add("abc")
    print(f"*****my_set的内容：{my_set},\tmy_set的地址{id(my_set)}")
my_set = {"x", "y", "z"}
print("-" * 30 + "set" + "-" * 30)
f3(my_set)
'''
打印如下：
------------------------------set------------------------------
*****my_set的内容：{'x', 'y', 'z'},	my_set的地址2176445895552
*****my_set的内容：{'x', 'y', 'z', 'abc'},	my_set的地址2176445895552
'''


# dict 数据类型是一种内置的可变、无序数据类型，用于存储键值对（key-value pairs）的集合。
# 字典通过键（key）快速查找对应的值（value），类似于现实中的词典（通过单词查找释义）
def f4(my_dict):
    print(f"*****my_dict的内容：{my_dict},\tmy_dict的地址{id(my_dict)}")
    my_dict["age"] = 25
    print(f"*****my_dict的内容：{my_dict},\tmy_dict的地址{id(my_dict)}")

print("-" * 30 + "dict" + "-" * 30)
my_dict = dict(name="George")
print(f"my_dict的内容：{my_dict},\tmy_dict的地址{id(my_dict)}")
f4(my_dict)
'''
打印如下：
------------------------------dict------------------------------
my_dict的内容：{'name': 'George'},	my_dict的地址2368587102976
*****my_dict的内容：{'name': 'George'},	my_dict的地址2368587102976
*****my_dict的内容：{'name': 'George', 'age': 25},	my_dict的地址2368587102976
'''