#第一题
lst = []
with open('D:/李空的下载/作业临时文件/hw.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        text = line.strip()
        if text == '':
            continue
        tcut = text[1:]
        lst.append(tcut)
    print('该文本文件共有{}行'.format(len(lst)))
    lgh = len(lst)

    co = 0
    for line in lst:
        if line[0] == 'P':
            co += 1
    print('其中以P开头的有{}行'.format(co))

    lst2 = []
    for lines in lst:
        lst2.append(len(lines))
    maxnum = lst2.index(max(lst2))+1
    minnum = lst2.index(min(lst2))+1
    print('包含字符最多的是第{}行'.format(maxnum))
    print('包含字符最多的是第{}行'.format(minnum))