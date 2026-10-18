#注意 本文件夹全部用Python3.12!

import requests
from lxml import html

with open('C:/Users/25162/PyCharmMiscProject/Robots/resourses.txt', 'r',encoding='utf-8') as f:
    linkrel_list = f.read()

#转化对象类型
document = html.fromstring(linkrel_list)
#xpath语法 用于获取某些内容
#获取表头
th_list = document.xpath('//thead/tr/th/text()')
print(th_list)
#获取表格
td_list = document.xpath('//tbody/tr/td/text()')
td_list1 = document.xpath('//tbody/tr/td[1]/text()')#每个个体的第n个元素
td_listA = document.xpath('//tbody/tr[1]/td/text()')#第n个个体
print(td_list)
print(td_list1)
print(td_listA,'\n')

#封装为细分的列表
#获取单个元素
tr_list = document.xpath('//tbody/tr')
print(th_list)
for tr in tr_list:
    print(tr.xpath('./td/text()'))