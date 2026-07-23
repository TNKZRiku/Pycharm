#字符串翻转和切片

#反转字符串
def str_receive(s):
    s_new = s[::-1]
    return s_new

if __name__ == '__main__':
    print(str_receive(input('input:')))

#字符串切片
def substr(s,x,y):
    ls = s[x:y]
    return ls

if __name__ == '__main__':
    a = input('1:')
    b = int(input('2:'))
    c = int(input('3:'))

    ls = substr(a,b,c)
    print(ls)
