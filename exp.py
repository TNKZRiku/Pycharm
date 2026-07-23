import os
from pyspark import SparkContext
from pyspark import SparkConf
os.environ['PYSPARK_DRIVER_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"

conf = SparkConf().setAppName("exp").setMaster('local[*]')
sc = SparkContext(conf=conf)

#内置了读取文件的方法
rdd1 = sc.textFile("D:/李空的下载/数据/rdd实例.txt")
#flatMap可以在读取文件的时候消除多行带来的影响
rdd2 = rdd1.flatMap(lambda line: line.split(" "))
#print(rdd2.collect())

#转化为kv进行计数
word_rdd = rdd2.map(lambda word: (word, 1))
#print(word_rdd.collect())
res_rdd = word_rdd.reduceByKey(lambda x, y: x + y)
print(res_rdd.collect())
