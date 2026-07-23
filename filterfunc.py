#fliter用于过滤数据
from pyspark import SparkContext
from pyspark import SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"

conf = SparkConf().setAppName("fliterfunc").setMaster('local[*]')
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1,2,3,4,5,6])
#传入的函数要输入一个值 返回一个布尔型
rdd2 = rdd1.filter(lambda x:x%2==0)
#print(rdd2.collect())

