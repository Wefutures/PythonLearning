# -*- coding: utf-8 -*-
"""写入文本"""
students = {
    "name": '张三'
}

# 写入时必须跟上编码格式
# 文字才有编码
# 数据流
with open('students.json', mode='w', encoding='utf-8') as f:
    # 必须写入字符串
    f.write(str(students))

# 二进制写入时，必须不能给编码 encoding
with open('hello', mode='wb') as f:
    # 必须写入字符串
    f.write(b'hello world !')
