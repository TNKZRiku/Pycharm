#方便函数传递参数时候的注释

#传参语法：def fun(变量1：类型)

def add1(a,b):
    return a+b

def add2(a:int,b:int):
    return a+b

a = 1
b = 2
aa = add2(a,b)
aaa = add1(a,b)

def func1(data):
    return data

#返回值类型注释语法：def fun(变量1：类型)->返回值的类型

def func(data:list)->list:
    return data

bb = func(1)
bbb = func1(1)

#注意 函数注解只是提示 不会影响运行

