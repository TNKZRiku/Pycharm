#常见语法

from lxml import html

with open('C:/Users/25162/PyCharmMiscProject/Robots/resourses.txt', 'r',encoding='utf-8') as f:
    cont = f.read()

document1 = html.fromstring(cont)

#/从根节点匹配
#//从任意节点匹配
th1 = document1.xpath('/html/body/table/thead/tr/th/text()')
print(th1)
th2 = document1.xpath('//tbody/tr/td/text()')
print(th2)
#输出第N个元素
th3 = document1.xpath('//tbody/tr[1]/td/text()')
print(th3)
#输出每个个体的第N个元素
th4 = document1.xpath('//tbody/tr/td[1]/text()')
print(th4)
#最后一个数据
th5 = document1.xpath('//tbody/tr[last()]/td/text()')
print(th5)

#匹配含有指定标签的元素
th6 = document1.xpath('//td[@class]/text()')
print(th6)
#*代表任意标签
th7 = document1.xpath('//*/td[@class]/text()')
print(th7)

