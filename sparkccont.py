#配置类对象

from pyspark import SparkContext
from pyspark import SparkConf

conf = SparkConf().setMaster('local[*]').setAppName('sparktest')
#第一个 代表本地运行
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1,2,3,4,5,6])
rdd2 = sc.parallelize((1,2,3,4,5,6))
rdd3 = sc.parallelize('string')
rdd4 = sc.parallelize({1,2,3,4,5,6})
rdd5 = sc.parallelize({'key1':'value1','key2':'value2'})

#用collect查看内容
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

rdd = sc.textFile("D:/李空的下载/数据/rdd读取.txt")

print(rdd.collect())
sc.stop()