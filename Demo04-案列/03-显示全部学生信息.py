# -*- coding: utf-8 -*-

students = [
    {'name': '张三', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '李四', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '赵六', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
]

print("姓名\t\t语文\t\t数学\t\t英语\t\t总分")
stu_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
for stu in students:
    print(stu_format.format(*stu.values()))