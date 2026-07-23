#复写可以修改继承得到的父类中的条目值
class Phone:
    imei = None
    porducer = 'heima'

    def callin4g(self):
        print('4G on')

class Phone2022(Phone):
    porducer = 'ITheima'

    def callin4g(self):
        print('手机已损坏')

phone = Phone2022()
phone2 = Phone()
phone.callin4g()
phone2.callin4g()
