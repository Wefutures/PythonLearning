# -*- coding: utf-8 -*-
"""字典定义"""

# 定义
dict1 = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75
}
# 复杂的字典
# - 键必须是唯一的
# - 值 可以取任何数据类型，但 键 只能使用 字符串、数字或 元组
dict2 = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75,
    1: 1,
    (0,): (0,),
    'dict': dict1,
    # [1]: [1]
}

print(dict2)
print(dict2["name"])

"""字典取值与修改"""
# 取值
print(dict2['dict'])

# 修改
dict1['height'] = 0
print(dict1)

# 键不存在时添加内容
dict1['weight'] = 120
print(dict1)

"""常用方法"""

# 当键不存在时报错
# print(dict1['sex'])
# get 当键不存在是默认返回空
print(dict1.get('sex'))
print(dict1.get('sex', '自定义不存在的返回值'))

# keys
print(dict1.keys())
print(dict1.values())
print("========")
print(dict1.items())

dict3 = {
    'sex': '男'
}
# 更新字典
dict1.update(dict3)
print(dict1)

# 遍历字典的键与值
for k, v in dict1.items():
    print(k, v)

for k in dict1.keys():
    print(k, dict1[k])

