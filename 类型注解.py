#进行注释
import json
import random

#基础注解：

var1:int = 1
var2:str = 'heima'
var3:bool = True

#简单注解：

mylist:list = [1,2,3,4,5]
mytuple:tuple = (1,2,3,4,5)
myset:set = {1,2,3,4,5}
mystr:str = '12345'
mydict:dict = {'1':'ture'}

#类对象注解：
class student:
    pass
stu:student = student()

#详细注解
mylist2:list[int] = [1,2,3,4,5]
#注意 元组需要列出所有元素的类型
mytuple2:tuple[int,str,bool] = (1,'heima',True)
#字典需要列出键值对的类型
mydict2:dict[int,bool] = {1:True,2:False}

#注释注解:
var4 = random.randint(1,10) #type:int
#注意 注释不是完全不被读取 type跟上类型可以进行注释
var5 = json.loads("{'name':'zhangsan'}") #type:dict[str,str]

def func():
    return 10
var6 = func() #type:int