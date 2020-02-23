# -*- coding: utf-8 -*-
# %%
# 整形
two = 2

# 查看变量的类型
print(two)
print(type(two))

# 浮点型（小数）
four = 4.0

# 查看变量的类型
print(four)
print(type(four))

""" 类型转化 """
print(float(two))

print(int(four))


"""数值运算"""
# %% 算术运行

# 加减乘除
print(two + four)
print(two - four)
print(two * four)
print(two / four)

# 取整、取余、取幂
print(two // four)
print(two % four)
print(two ** four)

# %% 赋值运算

two += two
print(two)
two -= two
print(two)
two *= two
print(two)
two /= four
print(two)

# %% 身份运算符
one = 1
o = 1
print(o is one)  # 变量驻存在内存中

a1 = [1]
a2 = [1]

print(a1 is a2)

print(id(o), id(one))
print(id(a1), id(a2))

# is 与 ==

print(a1 is a2)
print(a1 == a2)
