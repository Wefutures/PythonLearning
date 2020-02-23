# -*- coding: utf-8 -*-

"""布尔类型"""

print(4 > 5)
print(4 < 5)

"""布尔类型转化"""
# 数值型 ctrl + 鼠标左键
print(bool(1))
print(bool(1.0))
print(bool(0))

# 字符串类型
print(bool(" "))
print(bool(""))


# 函数与对象
def func():
    return 0


print(bool(func))
print(bool(func()))

"""运算符"""
# 比较运算
two = 2
four = 4
print(two >= four)
print(two <= four)
print(two != four)

# 错误写法
# print(two =< four)

# 逻辑运算
r = (5 > 4) and (6 > 5)
print(r)
print(True and True)
print(True or True)
print(True or False)
print(False or False)


# 运算符优先级
r = 4 > 2 ** 4 or True is 1 and '4' in "345"
if r:
    print('猜猜我的结果', r)
else:
    print('猜猜我的结果', r)

