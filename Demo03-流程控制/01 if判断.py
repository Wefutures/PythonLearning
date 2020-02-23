# -*- coding: utf-8 -*-

"""if else"""
sex = input("请输入你的性别：")

# if 语句以及缩进部分的代码也是一个完整的代码块0
if sex == "男":
    print("给你推荐男频小说")

# else 语句以及缩进部分的代码是一个完整的代码块
else:
    print("给你推荐女频小说")

""" if elif else"""
sex = input("请输入你的性别：")


if sex == "男":
    print("给你推荐男频小说")

elif sex == "女":
    print("给你推荐女频小说")

elif sex == "保密":
    print('不推荐')

else:
    print("给你推荐流行小说")

"""循环嵌套"""
sex = int(input("请输入你的性别："))

if sex == "男":
    print("给你推荐男频小说")
    hobby = int(input("请输入你的兴趣："))
    # 推荐男频小说的类别
    if hobby == '玄幻':
        print('给你推荐玄幻、修真、武侠小说')
    else:
        print('给你推荐默认的男频小说')
elif sex == "女":
    print("给你推荐女频小说")

elif sex == "保密":
    print('不推荐')

else:
    print("给你推荐流行小说")
