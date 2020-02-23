# -*- coding: utf-8 -*-

import json

while True:
    students = []

    name = input("请输入学生姓名:")
    chinese = input("请输入语文成绩:")
    math = input("请输入数学成绩:")
    english = input("请输入英语成绩:")

    total = int(chinese) + int(math) + int(english)

    info = {
        "name": name,
        "chinese": chinese,
        "math": math,
        "english": english,
        "total": total
    }
    students.append(info)
    # print(students)

    # 收集学生信息
    # {key:value} [[],[],[]] ((),(),())
    # 只存一个学生的信息
    # stu = ['张三', 65, 65, 65, 195]

    # 保存学生信息到本地
    with open("student.json", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(students))
    # 加载学生信息
    # with open("student.json", "r", encoding="utf-8") as f:
    #     data = f.read()
    #     students = json.loads(data)
    # print(students)
