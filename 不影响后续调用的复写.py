#调用复写之前的父内容
#第一种方法：父类名.函数/条目

class Phone:
    imei = None
    porducer = 'heima'

    def callin4g(self):
        print('4G已开启')

class Phone2022(Phone):
    porducer = 'ITheima'

    def callin4g(self):
        print('父类的厂商：{}'.format(Phone.porducer))
        print('父类的厂商：{}'.format(super().porducer))
        #super的含义就是父类名 通过这种方式不需要传递self参数
        print('开启通话模式')
        #print('4G已开启')
        Phone.callin4g(self)#这句话调用父类中的语句代替上一行
        super().callin4g()
        print('关闭通话模式')

phone = Phone2022()
phone.callin4g()