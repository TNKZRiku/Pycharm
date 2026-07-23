#__init__函数可以更快捷地制作类和对象

class Student:
    name = None
    age = None

    def __init__(self,name,age):#init会自动创建
        self.name = input('input your name:')
        self.age = age
        #这里其实会自动声明 上方不声明也可以
        print('创建了一个类对象')

stu1 = Student('周杰伦','24')
#之后 类对象的创建就像函数传参一样方便
print(stu1.name,stu1.age)