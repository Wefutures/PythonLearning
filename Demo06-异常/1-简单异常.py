# -*- coding: utf-8 -*-

# 整数异常
try:
    int(input("请输入一个整数："))
except Exception as e:
    print(e)
    print("类型转化出现错误")
    print("请输入数字")
