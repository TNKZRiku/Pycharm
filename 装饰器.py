#装饰器用来为一个函数增加新的功能
#需要注意的是 只能增加功能 而不能修改原函数
def sleep():
    import random
    import time
    print('正在睡觉')
    time.sleep(random.randint(1, 4))

#增加功能 睡前说‘我睡觉了’
#       起床说‘Ciallo’

def outer(defi):
    def inter():
        print('我睡觉了')
        defi()
        print('Ciallo')
    return inter

fn = outer(sleep)
fn()

#这是用闭包的思路来写 但是不够简洁 看上去像是调用了其他函数
#则可以把外部函数的函数名作为装饰器 以此看上去更优雅




