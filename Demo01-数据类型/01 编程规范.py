# -*- coding: utf-8 -*-
"""注释"""

# 单行注释

"""
多
行
注
释
"""

# ctrl + / 快速注释、取消注释
# 多
# 行
# 注
# 释

"""特殊注释"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


""" Python命名规则 """

hello_world = "hello world !"


# 类名用大驼峰 类与其他内容用两个换行隔开
class Student(object):

    # 变量名之间用空格隔开
    def __init__(self, hello):
        self.hello = hello

    # 函数与函数之间加换行
    def print_hello_world(self):
        """
        函数名用下划线命名法
        尽量满足见名知意
        """
        print(f"hello.jpg {self.hello} !")


# 变量名使用下划线命名法
# 尽量满足见名知意
# 对象也是变量
student = Student("world")
student.print_hello_world()
