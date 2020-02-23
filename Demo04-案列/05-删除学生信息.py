# -*- coding: utf-8 -*-



students = [
    {'name': '张三', 'chinese': '84', 'math': '95', 'english': '65', 'total': 195},
    {'name': '李四', 'chinese': '60', 'math': '68', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '75', 'math': '79', 'english': '65', 'total': 195},
    {'name': '赵六', 'chinese': '99', 'math': '65', 'english': '65', 'total': 195},
]

name = input("请输入学生姓名:")

for stu in students:
    if name == stu["name"]:
        # del 删除指定位置内容 remove指定内容进行删除 pop弹出
        # students.remove(stu)
        students.pop(students.index(stu))
        # print(stu)
        print(f"{name}同学的信息已删除!!!")
        break
else:
    print("该学生不存在！！！")

