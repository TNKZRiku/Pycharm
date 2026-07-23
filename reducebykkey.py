#rbk可以对于kv型rdd进行按组运算 运算逻辑来自用户
#分组是按k自动的
#以加和为例
from pyspark import SparkContext
from pyspark import SparkConf

import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('reducebykey')
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([('男',60),('男',62),('女',63),('女',64)])
#V,V -> V
rdd2 = rdd1.reduceByKey(lambda a,b:a+b)
print(rdd2.collect())

