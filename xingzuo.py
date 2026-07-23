#第二题
import csv

lst = []
with open("D:/李空的下载/作业临时文件/xz.csv","r",encoding='utf - 8') as f:
    text = csv.reader(f)
    for row in text:
        if len(row) < 2:
            continue
        #print(row)
        lst.append(row)
    #print(lst)

    while True:
        inp = str(input('\n请输入你的星座:'))
        if inp == 'q' or inp == 'Q':
            print('程序退出')
            break
        else:
            for line in lst:
                if inp == line[0]:
                    cste = line[0]
                    sta = line[1]
                    end = line[2]
                    msta = sta[0:1]
                    dsta = sta[1:]
                    mend = end[0:1]
                    dend = end[1:]
                    sig = chr(int(line[3]))
                    print('你的星座{}从{}月{}日开始，{}月{}日结束，对应符号{}'.format(cste,msta,dsta,mend,dend,sig))
                    break
            else:
                print('输入星座名有误！')


