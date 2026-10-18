#csv需要gbk编码
#csv用逗号分隔
import csv
with open('D:/李空的下载/数据/csv.csv','w',encoding='gbk') as f:
    f.write('原神,2020,米哈柚')
    f.write('绝区零,2024,银灰物品')

#另一种写入
with open('D:/李空的下载/数据/csv2.csv','w',encoding='utf-8') as f:
    whiter = csv.DictWriter(f,fieldnames=['游戏名','年份','出品商'])
    whiter.writeheader()
    whiter.writerow({'游戏名':"原神",'年份':2020,'出品商':'米哈柚'})
    whiter.writerow({'游戏名': "绝区零", '年份': 2024, '出品商': '银灰物品'})

with open('D:/李空的下载/数据/csv2.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
