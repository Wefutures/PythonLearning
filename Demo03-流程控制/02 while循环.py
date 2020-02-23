# -*- coding: utf-8 -*-

print('hello world !')
print('hello world !')
print('hello world !')
print('hello world !')
print('hello world !')

"""while 循环"""
i = 0  # 限制条件
while i < 5:  # 循环申明 判断条件
    print('hello world !')  # 程序执行的内容
    i += 1  # 限制条件

# 直角三角形
i = 1
while i < 6:
    print('*' * i)
    i += 1

# 循环打印直角三角形
i = 1
while i < 6:
    # print('*')
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1

"""九九乘法表"""
i = 1
while i < 9:
    j = 1
    while j < i:
        # print(f"{j}*{i}={i*j}\t", end="")
        # print("{}*{}={}".format(j, i, i * j), "\t", end="")
        print("%d * %d = %d" % (j, i, i * j), "\t", end="")
        j += 1
    print()
    i += 1
