
# coding=UTF-8


class Student():
    sum = 0
    def __init__(self, name, age):
        # name = name
        # age = age
        self.name = name  #定义实例变量
        self.age = age  #定义实例变量
        print(self.name) #操作实例变量
        # **************访问类变量的方法
        print(Student.sum) 
        print(self.__class__.sum)
    def do_homework(self):
        print('homework')

student1 = Student('tom', 18)
student2 = Student('Joy', 18)
# print(student1.name)  
# print(student2.name)  
# print(Student.name)
