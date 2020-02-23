# -*- coding: utf-8 -*-
"""字符串创建"""

# 单引号、双引号
s1 = 'hello world !'
s2 = "hello world !"
print(s1 is s2)

s3 = """hello world !"""
print(s1 is s2 is s3)

# 多行字符串
s4 = """
hello world !
"""

print(s1 is s4)

"""转义字符"""
# 单、双引号实现跨行
print('hello \
    world !')

# 原始字符 不允许特殊字符进行转义 unicode utf-8 gbk
print(r'hello \n world !')

"""
常见的特殊字符(正则)
\ / ? [ ] ( ) ' ....

\t(四个空格键) \n（换行） \b \r ....
\r\n windows中的换行
\n Linux下的换行

一个反斜杠是特殊字符
两个反斜杠 才是反斜杠本身
"""

"""字符串格式化"""
name = '张三'
name2 = '李四'

# %s 用 %s 占位
print('hello %s !' % name)
# 多个参数
print('hello %s %s !' % (name, name2))
print('hello %s\nhello %s !' % (name, name2))

# %d
print('hello %d hello %s !' % (66, name2))


# format 用 {} 占位
print('hello {} !'.format(name))
print('hello {} {} !'.format(name, name2))
print('hello {}\nhello{} !'.format(name, name2))
print('hello {name}\nhello{name2} !'.format(name2=name, name=name2))

# f 在字符串中嵌入变量
print(f'hello {name} !')

# 字符格式化输出（比较少用）
# 对齐输出 > < ^
print('hello {}'.format(name))
print('hello {:>10}'.format("李四"))

# 保留小数位位数
print('{:.5f}'.format(10 / 3))

#
print('%s' % 10)


"""
顾首不顾尾
"""
