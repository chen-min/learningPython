
# coding=UTF-8

class Student():
    sum = 0
    def __init__(self, name, age):
        self.name = name  
        self.age = age  
    def do_homework(self):
        print('homework')

    #定义一个类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        #print(self.name)  不能访问实例变量

    @staticmethod
    # 不用强制传入self/cls等默认参数
    def add(x,y):
        print('this is a static method')
        #print(self.name) 不能访问实例变量

student1 = Student('tom', 18)
student1.add(1,2)  #静态方法可以同时被对象和类调用
Student.add(1,2)
student1.plus_sum()


# coding=UTF-8

class Student():
    sum = 0
    def __init__(self, name, age):
        self.name = name  
        self.age = age  
        self.__score = 0
    
    def marking(self, score):
        if score < 0:
            return '不能输入负分'
        self.__score = score
        print(self.name + '本次考试分数' + str(self.__score))


student1 = Student('tom', 18)
result = student1.marking(10)  #通过方法对数据修改, 比对数据直接进行修改安全些
# print(result)
student1.__score = -1
print(student1.__dict__)
