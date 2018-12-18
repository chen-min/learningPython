# coding=UTF-8


class Student():
    name = ''   
    age = 0
    def __init__(self, name, age):
        #构造函数
        #初始化对象的属性
        name = name
        age = age
        print('student')
    #行为 与 特征
    def do_homework(self):
        print('homework')

# 实例化
student1 = Student('tom', 18)
print(student1.name)  # 这样打印出来是空值, 为什么
# a = student1.__init__()
# print(a)  # 返回为空
# print(type(a))
#构造函数不能强制返回, 只能返回None