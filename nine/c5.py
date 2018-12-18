
# coding=UTF-8

from c6 import Human

class Student(Human):
    def __init__(self, school, name, age):
        self.school = school  
        super(Student, self).__init__(name, age) 
        # #主流调用方式

    def do_homework(self):
        super(Student, self).do_homework()
        print('homework')

student1 = Student('university', 'Tim', 18)
student1.do_homework()