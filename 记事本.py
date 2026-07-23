import os

f = open('D:/李空的下载/作业临时文件/hw.txt','r',encoding='utf-8')
oldline = f.read().splitlines()
line = [lines for lines in oldline if lines.strip()!='']
print(line)

lcount = len(line)
pcount = 0
for line1 in line:
    line2 = line1.strip()
    if line2.startswith('P'):
        pcount += 1
long = []
for line3 in line:
    length = len(line3.rstrip('\n'))
    long.append(length)
longest = max(long)
short = min(long)

print('该文本文件一共有{}行'.format(lcount))
print('文件中以大写字母P开头有{}行'.format(pcount))
print('字符最多的是第{}行'.format(longest+1))
print('字符最少的是第{}行'.format(short+1))