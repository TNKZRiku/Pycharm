#一个同样的函数 传入不同的目标 会得到不同的结果
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("I am dog.")

class Cat(Animal):
    def speak(self):
        print("I am cat.")

def func(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()

func(dog)
func(cat)



