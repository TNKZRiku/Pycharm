#可以借助thread模块进行多线程并行
#创建实例 传入参数([,group[,target[,name[,args[,kwargs]]]]])
import threading
from time import sleep
import random

def srbk(msg):
    while True:
        print('我在玩千恋*万花')
        print(msg)
        sleep(random.randint(1,3))
def rj(msg):
    while True:
        print('我在玩密命王牌')
        print(msg)
        sleep(random.randint(1,3))

srbk_thread = threading.Thread(target=srbk,args=('千恋*万花真好玩',))
rj_thread = threading.Thread(target=rj,kwargs={'msg':'密命王牌真好玩'})
#两种传参方式 元组需要按位置传参 如果只传一个 需要额外加逗号
#字典传参则key为形参名
srbk_thread.start()
rj_thread.start()