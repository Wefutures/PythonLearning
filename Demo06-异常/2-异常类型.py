# -*- coding: utf-8 -*-


# 尝试
try:
    num = int(input("请输入一个整数："))  # ValueError
    a = 8 / num  # ZeroDivisionError
# 捕捉类型错误
except ValueError:
    print("请输入一个数字")
except ZeroDivisionError:
    print("输入的数不能为零")
except:
    print("其他错误")

