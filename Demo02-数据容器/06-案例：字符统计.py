# -*- coding: utf-8 -*-
"""
统计Python之禅中所有字符出现的次数
"""
# python 之禅
this_str = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

d = {}

for i in this_str:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

for k, v in d.items():
    print(f"字符 {k} 出现了 {v} 次")

# 拓展：对字典进行排序输出

# 1. 字典是无序的，需要改变结构
l = list(d.items())


def func(temp):
    return temp[1]


# 2. 需要指定列表里面的元素的第二个值进行排序
l.sort(key=func, reverse=True)

print(l)
for i in l:
    print(f"字符 {i[0]} 出现了 {i[1]} 次")
