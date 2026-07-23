#sortBy可以按照某个参数进行排序 默认为升序
from pyspark import SparkContext
from pyspark import SparkConf

import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('sortbyfunc')
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize((['a',2,'abc'],['b',4,'def'],['c',3,'plk']))
#其中第一个参数要传入一个函数 来返回'根据谁来排序'
rdd2 = rdd1.sortBy(lambda x : x[1],ascending=True,numPartitions=1)
print(rdd2.collect())
