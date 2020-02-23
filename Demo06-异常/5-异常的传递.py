# -*- coding: utf-8 -*-


# # 触发异常
# def _test_raise(number):
#     if number < 1:
#         raise ValueError('Invalid value')  # 或者 raise ValueError,'Invalid value'
#
#
# _test_raise(0)

# 异常的传递性
def demo2():
    num = int(input('请输入一个数'))
    print(1 / num)


def demo1():
    demo2()


demo1()

# try:
#     demo1()
# except Exception as e:
#     print(e)
