#闭包
#闭包可以让一个函数依赖一个外部参数而不会产生全局变量

def outer(defi):
    def inter (prmt):
        print('{}{}'.format(defi,prmt))

    return inter

#在这段代码中 第一次调用会返回一个名为inter的函数 而不是值
#此时 返回函数的defi参数就会固定为第一次传入的内容
#之后 再调用这个（接受了返回值的函数）进行运行

Asa = outer('早安!')
Ban = outer('晚安!')
#修改外部变量重新赋值 创建新的函数即可

Asa('Ciallo')
Asa('Onani')
Ban('Ciallo')
Ban('Onani')

#需要注意 无法直接在内部访问外部变量
def outer2(num1):
    def inter (prmt):
        num1 += prmt

#添加nonlocal关键字解除限制
def outer3(num1):
    def inter (prmt):
        nonlocal num1
        num1 += prmt
        print(num1)
    return inter

atm = outer3(0)
atm(100)
atm(200)
#能够修改

