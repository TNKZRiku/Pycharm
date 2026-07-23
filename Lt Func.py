class Student1():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __lt__(self, other):#传入参数 其他类的某个值
        return self.age < other.age#这里返回bool

stu1 = Student1('林俊杰',24)
stu2 = Student1('周杰伦',28)
print(stu1 < stu2)
