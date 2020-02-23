# -*- coding: utf-8 -*-

students = [
    {'name': '张三', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '李四', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '赵六', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
]
stu_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"


print("(输入为空就使用之前的值)")
name = input("请输入学生姓名")

# 查询学生信息
for std in students:
    # 如果学生存在
    if name == std['name']:
        # 如果学生存在 就修改学生信息
        name = input("请输入学生姓名：")
        chinese = input("请输入语文成绩：")
        math = input("请输入数学成绩：")
        english = input("请输入英语成绩：")

        # 字典的重新复制 指定已经存在的键 跟新 value
        # if 判断一下 之前有没有输入过这个内容
        if name:
            std['name'] = name
        if chinese:
            std['chinese'] = chinese
        if math:
            std['math'] = math
        if english:
            std['english'] = english

        std['total'] = int(std['chinese']) + int(std['math']) + int(std['english'])

        break
else:
    print("该学生不存在")
print(students)
