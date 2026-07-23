#"D:\李空的下载\数据\rdd实例2.txt"
#{'id': 1, 'timestamp': '2019-05-08T01:03.00Z',
# 'category': '平板电脑', 'areaName': '北京', 'money': '1450'}
#目的：1 统计各地营业额并降序排列
#     2 统计总商品种类
#     3 统计北京的商品种类

import json
from pyspark import SparkContext
from pyspark import SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"
conf = SparkConf().setAppName("exp2").setMaster('local[*]')
sc = SparkContext(conf=conf)

path = "D:/李空的下载/数据/rdd实例2.txt"
file_rdd = sc.textFile(path)
text_rdd = file_rdd.flatMap(lambda line: line.split('|'))
json_rdd = text_rdd.map(lambda line:json.loads(line))
tup_rdd = json_rdd.map(lambda x:(x['areaName'],int(x['money'])))
#[ ('北京', '1450'), ('北京', '8412'), ('上海', '1513'),...
res1 = tup_rdd.reduceByKey(lambda a,b: a+b)
res1_sort = res1.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
#[('郑州', 1120), ('上海', 1513),
#('天津', 12260), ('杭州', 28831), ('北京', 91556)]
cont1 = res1_sort.collect()
for i in cont1:
    print('{}的营业额为{}元'.format(i[0],i[1]))

tup2_rdd = json_rdd.map(lambda line:line['category'])
res2 = tup2_rdd.distinct()
cont2 = res2.collect()
#print(cont2)
co = 0
print('一共出现的商品种类：',end='')
for i in cont2:
    co += 1
    if co == len(cont2):
        print(i,end='')
    else:
        print(i,end=',')
print('')

tup3_rdd = json_rdd.map(lambda x:(x['areaName'],(x['category'])))
#[('北京', '手机'), ('北京', '手机'), ('上海', '电脑'),
res3 = tup3_rdd.filter(lambda x:x[0] == '北京')
#[('北京', '平板电脑'), ('北京', '手机'), ('北京', '手机'),
cont3 = res3.distinct()
cont31 = cont3.collect()
co2 = 0
print('北京销售的全部类型：',end='')
for i in cont31:
    co2 += 1
    if co2 == len(cont31):
        print(i[1],end=' ')
    else:
        print(i[1],end=',')