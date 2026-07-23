#封装不被外部使用 但是可以被内部调用
class Phone():
    code = None
    char = None

    def __ram(self):
        print('修改内存调度节省电量')

    def call_by_5G(self):
        if self.char >= 1:
            print('5G on')

        else:
            self.__ram()

phone1 = Phone()
phone1.char = 0.5
phone1.call_by_5G()