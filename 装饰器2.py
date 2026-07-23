#在定义函数的上方声明装饰器（外层函数）
#即可直接调用原函数

def outer(func):
    def inner():
        print('我睡觉了')
        func()
        print('Ciallo')
    return inner

@outer
def sleep():
    import time
    import random
    print('睡觉中....')
    time.sleep(random.randint(1,4))

sleep()
#装饰器的作用就是让这个拓展过的函数看上去还像之前一样