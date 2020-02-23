# -*- coding: utf-8 -*-
"""for 遍历"""
for i in 'hello world !':
    print(i)

for i in range(10):
    print(i)

"""range"""

ran1 = range(0, 10)
ran2 = range(0, 10, 1)
ran3 = range(0, 10, 2)

print(ran1)
print(ran2)
print(ran3)
# 把可迭代对象转化为列表
print(list(ran1))
print(list(ran2))
print(list(ran3))

"""for 实现九九乘法表"""
for i in range(1, 10, 1):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j*i}\t", end='')
    print()
