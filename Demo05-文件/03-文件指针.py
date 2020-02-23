# -*- coding: utf-8 -*-
file = open("this.txt", encoding='utf-8')

text = file.read()
print(text)

"""文件指针 指向最开始，可以重新读取"""
file.seek(0, 0)

text = file.read()
print(text)

file.close()
