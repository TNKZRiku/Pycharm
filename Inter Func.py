#str函数：把对象的输出可视化
class Student1():
    def __init__(self,name,age):
        self.name = name
        self.age = age

stu1 = Student1('周杰伦',24)
print(stu1)
print(str(stu1))

class Student2():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{} {}'.format(self.name,self.age)
    #本质上是规定了这个对象的输出内容
stu2 = Student2('周杰伦',24)
print(stu2)
print(str(stu2))



