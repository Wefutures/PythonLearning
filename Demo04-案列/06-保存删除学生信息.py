# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import json

students = [
    {'name': '张三', 'chinese': '84', 'math': '95', 'english': '65', 'total': 195},
    {'name': '李四', 'chinese': '60', 'math': '68', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '75', 'math': '79', 'english': '65', 'total': 195},
    {'name': '赵六', 'chinese': '99', 'math': '65', 'english': '65', 'total': 195},
]


# 保存被删除学生的信息
stu_del_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"

name = input("请输入学生姓名:")

for stu in students:
    if name == stu["name"]:
        # del 删除指定位置内容 remove指定内容进行删除 pop弹出
        # students.remove(stu)
        with open("stu_del_format.json","w",encoding="utf-8") as f:
            f.write("姓名\t\t语文\t\t数学\t\t英语\t\t总分"+"\n")
            f.write(json.dumps(stu_del_format.format(*stu.values())))
        # print(stu_del_format.format(*stu.values()))
        students.pop(students.index(stu))
        print(stu)
        print(f"{name}同学的信息已删除!!!")
        break
else:
    print("该学生不存在！！！")

