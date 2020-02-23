# -*- coding: utf-8 -*-
# 集合创建
set1 = {1, 2, 2, 3, 5, 6, 4, 4}
print(set1)

# 集合对列表进行去重
li = [1, 2, 2, 3, 5, 6, 4, 4]
li = list(set(li))
print(li)

"""集合运算（了解）"""
set2 = {2, 3, 4}
set3 = {3, 4, 5}
# 交 and
print(set2 & set3)
# 并 or
print(set2 | set3)
# 差 相减
print(set2 ^ set3)
