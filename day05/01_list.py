# list数据结构的使用

# list 索引也可以从尾部开始，最后一个元素的索引为-1， 往前一位为-2，以此类推
list = [1, 2, 3, 4]
# print(list[-1]) # 4
# print(list[-4]) # 1
# print(list[0]) # 1

list.append(5)

print("\n--------------- 从列表中删除元素 ---------------\n")
# 从列表中删除元素（不允许的做法）
# for ele in list:
#     if ele == 2:
#         list.remove(1)
# print(list)

# 推荐的做法
# list[:] 是 Python 中**列表切片（slicing）**的一种特殊写法，意思是： 从头到尾取这个列表的所有元素，从而创建一个新列表（浅拷贝）
for x in list[:]:
    if x == 2:
        list.remove(1)
print(list)   # 输出: [1, 3, 4, 5]



# 对于大数据量，原地删除，更加节约内存
lst = [10, 20, 30, 20, 40, 20, 50]
# range(start， stop， step)
for i in range(len(lst)-1, -1, -1):   # 从最后一个往前
    if lst[i] == 20:
        lst.pop(i)                    # 或者 del lst[i]
        # del lst[i]
print(lst)   # [10, 30, 40, 50]


print("\n--------------- 列表的常用操作 ---------------\n")