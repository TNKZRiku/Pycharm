#创建大量类对象的时候 可以使用工厂模式
#传统创建
class persont:
    pass
class workert(persont):
    pass
class teachert(persont):
    pass
class studentt(persont):
    pass

workert = workert()
teachert = teachert()
studentt = studentt()

#工厂模式
class person:
    pass

class Worker(person):
    pass
class Teacher(person):
    pass
class Student(person):
    pass


class factory():
    def get_person(self,job):
        if job == 'w':
            return Worker()
        elif job == 't':
            return Teacher()
        else:
            return Student()

Factory = factory()
worker = Factory.get_person('w')
teacher = Factory.get_person('t')
student = Factory.get_person('s')

print(type(worker))

#优点是如果某个类的构造改了 那么在修改实例的时候会很方便 直接修改工厂内的代码就行
#工厂模式能够统一入口 降低维护成本 发生修改时 只需要修改工厂类就可以

