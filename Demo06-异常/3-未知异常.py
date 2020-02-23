# -*- coding: utf-8 -*-


# 位置类型异常
try:
    num = int(input("请输入一个整数："))  # ValueError
# 异常类
except Exception as e:
    print("出现了一个错误", e)
