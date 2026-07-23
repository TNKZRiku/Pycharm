#私有变量和私有函数可以通过前面写两个下划线实现
class Phone():
    code = None
    prod = None
    __elec = None

    def use5g(self):
        print('5G using')

    def __ram(self):
        print('ram change')

phone1 = Phone()

print(phone1.elec)
print(phone1.__elec)
print(phone1.code)
phone1.ram()
phone1.__ram()
phone1.use5g()
#私有内容无法被调用 也无法赋值 会报错