# -*- coding: utf-8 -*-
"""列表"""
tuple1 = (1, 2, 3, 4, 5, 6, 7)

# 元组中可以存放多种数据
array2 = (1, 2, 3, True, False, int, "str", tuple1)
print(array2)

"""转化其他序列为元组"""
# 转化字符串
print(tuple('hello.jpg world !'))
# 转化列表
print(tuple(list('hello.jpg world !')))


# 元组取值
# 取列表的第一个值
print(tuple1[0])

"""不可变数据类型-元组"""
# tuple1[0] = 10
# print(tuple1[0])


"""元组切片"""

# 指定区间切片
print(tuple1[2:5])
print(tuple1[2:-2])

# 从头开始切片
print(tuple1[0:5])

# 切片到末尾
print(tuple1[0:])

# 省略参数切全部内容
print(tuple1[:])

# 指定步长切片
print(tuple1[0:5:1])
print(tuple1[0:5:2])
