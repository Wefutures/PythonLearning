# -*- coding: utf-8 -*-
"""列表常用方法"""

array1 = [1, 2, 3, 4, 5]

# insert 第一个参数是插入位置，第二个参数是插入的内容
array1.insert(0, '0')
print(array1)

# append 添加元素到末尾
array1.append('6')
print(array1)

# pop 默认弹出末尾内容
pop = array1.pop()
print(pop)
print(array1)

# pop 指定索引弹出内容
pop = array1.pop(0)
print(pop)
print(array1)

# 就地排序（修改原有列表）
array1.sort(reverse=True)
print(array1)

# 排序后返回一个新的列表（不修改原有列表）
arr = sorted(array1)
print(arr)
print(array1)

"""其他方法"""
# 使用in判断值是否存在
print(2 in array1)
# 使用 += 合并列表（返回一个新列表）
arr += array1
print(arr)
# 使用 len() 获取长度
print(len(arr))
# 使用join()转换为字符串
print(','.join(['1', '2', '3']))

"""元组常用方法"""

"""字符串常用方法"""
s = '\n # hello.jpg world ! # \n\r'
# print(s)
#
# # 去掉两端空白字符
# print(s.strip())
# # 继续去掉 #
# new_s = s.strip()
# print(new_s.strip("#"))
#
# # 支持链式调用 一个套一个
# print(s.strip().strip("#").strip())

# 替换
# print(s.replace('#', "").strip())

# 分割
print(s.split())
print(s.split("#"))

# 合并
print(",".join(s.split()))
# 错误用法
# print(",".join([1, 2, 3, 4]))

"""解包"""

# 元组解包
a, b, c = (1, 2, 3)
print(a, b, c)

# 列表解包
a, b, c = [1, 2, 3]
print(a, b, c)

# 生成器解包
a, b, c = range(1, 4)
print(a, b, c)

# 字符串解包
a, b, c = '123'
print(a, b, c)

# 用 _ 收集不用的变量（了解）
_, _, c = tuple('abc')

# 另外一种解包方式
print(*range(10))
