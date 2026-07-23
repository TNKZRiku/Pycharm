#实现一个存取钱功能
def atm(amount = 0):
    def inorput(money,deposit = True):
        nonlocal amount
        if deposit:
            amount += money
            print('本次存钱{}元 余额{}元'.format(money,amount))
        else:
            amount -= money
            print('本次取钱{}元 余额{}元'.format(money,amount))
    return inorput

Atm = atm()
Atm(100)
Atm(200)
Atm(300)
Atm(200,False)


