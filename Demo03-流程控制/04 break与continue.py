# -*- coding: utf-8 -*-
"""break"""
while True:

    password = input("请输入密码")
    if password == '123456':
        # 当满足条件时 中断循环
        print('密码输入正确，跳出循环')
        break

    # 重复执行的代码
    print("输入的密码错误，请重新输入")

"""continue"""

# while True:
#
#     password = input("请输入密码")
#     if password == '123456':
#         # 当满足条件时 终止后续的操作
#         print('密码输入正确，终止后续的操作')
#         continue
#
#     print("输入的密码错误，请重新输入")


"""else"""
i = 1
while i < 5:
    i += 1
else:
    print('正常结束')


for i in range(5):
    pass
else:
    print('正常结束')
