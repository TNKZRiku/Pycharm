#最后一次作业
class Ject:
    def __init__(self,id,namae,sensei):
        self.Jid = id
        self.Jnamae = namae
        self.Jsensei = sensei
        self.__Jbashou = '上课地点'

    def check(self):
        print('课程编号：{}，课程名称：{}，任课老师：{}，上课地点：{}'.format(self.Jid,self.Jnamae,self.Jsensei,self.__Jbashou))





