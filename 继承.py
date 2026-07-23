#继承可以做到类似追加条目的效果
#class类（父类）
class Phone:
    imei = None
    porducer = 'heima'

    def callin4g(self):
        print('4G on')

class Phone2022(Phone):
    face_id = '10001'

    def callin5g(self):
        print('5G on')

phone = Phone2022()
print(phone.porducer)#2022中没有厂商 但是继承来的 所以有
phone.callin4g()
phone.callin5g()
