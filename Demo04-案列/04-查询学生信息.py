# -*- coding: utf-8 -*-

students = [
    {'name': '张三', 'chinese': '84', 'math': '95', 'english': '65', 'total': 195},
    {'name': '李四', 'chinese': '60', 'math': '68', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '75', 'math': '79', 'english': '65', 'total': 195},
    {'name': '赵六', 'chinese': '99', 'math': '65', 'english': '65', 'total': 195},
]

stu_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
name = input("请输入学生姓名:")

for stu in students:
    if name == stu["name"]:
        print("姓名\t\t语文\t\t数学\t\t英语\t\t总分")
        print(stu_format.format(*stu.values()))
        break
else:
    print("该学生不存在!!!")

