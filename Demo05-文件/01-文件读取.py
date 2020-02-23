# -*- coding: utf-8 -*-
# 1. 打开 - 文件名需要注意大小写
file = open("this.txt", encoding='utf-8')

# 2. 读取
text = file.read()
print(text)

# 2.1 读取一行
line = file.readline()
# 2.2 读取多行
lines = file.readlines()

# 3. 关闭
file.close()
