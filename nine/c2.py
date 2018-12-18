# coding=UTF-8


class Student():
    name = 'qiyue'   #类变量
    age = 0
    def __init__(self, name, age):
        # name = name
        # age = age
        self.name = name  #定义实例变量
        self.age = age  #定义实例变量
        print(name)
        print(age)
        # print('student')
    def do_homework(self):
        print('homework')

student1 = Student('tom', 18)
student2 = Student('Joy', 18)
# print(student1.name)  
# print(student2.name)  
# print(Student.name)
