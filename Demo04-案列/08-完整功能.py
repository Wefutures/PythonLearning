# -*- coding: utf-8 -*-

import json

str_message = """
**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 删除学生信息
5. 修改学生信息

0. 退出系统
**************************************************
"""



with open("student.json", "r", encoding="utf-8") as f:
    data = f.read()
students = json.loads(data)

stu_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
stu_del_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"

while True:
    print(str_message)
    action = input()

    if action == "0":
        print("欢迎再次使用学生信息管理系统")
        break

    elif action == "1":
        # students = []
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

        # 保存学生信息到本地
        with open("student.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(students))

    elif action == "2":
        print("姓名\t\t语文\t\t数学\t\t英语\t\t总分")
        for stu in students:
            print(stu_format.format(*stu.values()))

    elif action == "3":
        # stu_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
        name = input("请输入学生姓名:")

        for stu in students:
            if name == stu["name"]:
                print("姓名\t\t语文\t\t数学\t\t英语\t\t总分")
                print(stu_format.format(*stu.values()))
                break
        else:
            print("该学生不存在!!!")

    elif action == "4":
        name = input("请输入学生姓名:")
        # 保存被删除学生的信息
        for stu in students:
            if name == stu["name"]:
                # del 删除指定位置内容 remove指定内容进行删除 pop弹出
                # students.remove(stu)
                with open("stu_del_format.json", "a", encoding="utf-8") as f:
                    f.write("姓名\t\t语文\t\t数学\t\t英语\t\t总分" + "\n")
                    f.write(json.dumps(stu_del_format.format(*stu.values())))
                # print(stu_del_format.format(*stu.values()))
                students.pop(students.index(stu))
                print(stu)
                print(f"{name}同学的信息已删除!!!")
                break
        else:
            print("该学生不存在！！！")

    elif action == "5":
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
        # 出了上面出现的情况之外的其他情况
    else:
        print("请输入正确的操作")





# # -*- coding: utf-8 -*-
# import json
#
# str_message = """**************************************************
# 欢迎使用【学生信息管理系统】V1.0
# 请选择你想要进行的操作
# 1. 新建学生信息
# 2. 显示全部信息
# 3. 查询学生信息
# 4. 删除学生信息
# 5. 修改学生信息
#
# 0. 退出系统
# **************************************************
# """
#
# with open('student.json', mode='r', encoding='utf-8') as f:
#     text = f.read()
# # 全局变量
# students = json.loads(text)
# str_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
# while True:
#     print(str_message)
#     action = input()
#     if action == '0':
#         print("欢迎再次使用学生信息管理系统")
#         break
#     elif action == '1':
#         name = input("请输入学生姓名：")
#         chinese = input("请输入语文成绩：")
#         math = input("请输入数学成绩：")
#         english = input("请输入英语成绩：")
#
#         total = int(chinese) + int(math) + int(english)
#         d = {
#             'name': name,
#             'chinese': chinese,
#             'math': math,
#             'english': english,
#             'total': total
#         }
#         students.append(d)
#     elif action == '2':
#         print("姓名\t\t语文\t数学\t英语\t总分")
#         for student in students:
#             print(str_format.format(*student.values()))
#     elif action == '3':
#         name = input("请输入学生姓名")
#
#         for student in students:
#             if name == student['name']:
#                 print("姓名\t\t语文\t数学\t英语\t总分")
#                 print(str_format.format(*student.values()))
#                 break
#         else:
#             print("该学生不存在")
#     elif action == '4':
#         name = input("请输入学生姓名")
#
#         for student in students:
#             if name == student['name']:
#                 print('下面这个学生的信息已经被删除')
#                 print(students.pop(students.index(student)))
#                 break
#         else:
#             print("该学生不存在")
#         print(students)
#     elif action == '5':
#         print("(输入为空就使用之前的值)")
#         name = input("请输入学生姓名")
#         for student in students:
#             if name == student['name']:
#                 name = input("请输入学生姓名：")
#                 chinese = input("请输入语文成绩：")
#                 math = input("请输入数学成绩：")
#                 english = input("请输入英语成绩：")
#                 if name:
#                     student['name'] = name
#                 if chinese:
#                     student['chinese'] = chinese
#                 if math:
#                     student['math'] = math
#                 if english:
#                     student['english'] = english
#
#                 student['total'] = int(student['chinese']) + int(student['math']) + int(student['english'])
#                 break
#         else:
#             print("该学生不存在")
#         print(students)
#     # 出了上面出现的情况之外的其他情况
#     else:
#         print("请输入正确的操作")

