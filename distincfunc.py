#distinct用于去重 无需传参 但是需要接收
from pyspark import SparkContext
from pyspark import SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"

conf = SparkConf().setAppName("fliterfunc").setMaster('local[*]')
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1,1,2,4,5,3,4,6,5,6,3,2,5,4,1])
rdd2 = rdd1.distinct()
print(rdd2.collect())