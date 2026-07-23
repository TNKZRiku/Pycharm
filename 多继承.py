#可以继承多个父类
class Phone:
    imei = None
    porducer = 'heima'

    def callin4g(self):
        print('4g on')

class nfc:
    nfc = '第五代'
    porducer = 'heima'

    def nfcreader(self):
        print('nfc read')

    def nfcwriter(self):
        print('nfc write')

class remote:
    rc = '红外遥控'

    def control(self):
        print('remote control on')

class MyPhone(Phone,remote,nfc):
    pass#如果已经继承足够的话就写个pass

phone = MyPhone()
phone.callin4g()
phone.nfcreader()
phone.nfcwriter()
phone.control()
