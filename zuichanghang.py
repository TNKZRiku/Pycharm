#第三题

lst = []
with open('D:/李空的下载/作业临时文件/sample.txt', 'r',encoding='utf - 8') as f:

    for row in f:
        text = row.replace('\u200f','')
        #lst.append(text)
        #lst.append(text)#strip删除空行 但是会留下无内容空格
        if not text:
            continue
        lst.append(text)
    #print(lst)

    #print(lst)
    maxcon = max(lst)
    maxlen = len(maxcon)
    print(maxlen,maxcon)








