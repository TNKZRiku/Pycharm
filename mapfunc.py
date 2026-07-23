#借助map算子完成运算
from pyspark import SparkContext
from pyspark import SparkConf
#目前只有pyc能调用解释器 而spark是找不到解释器的！需要手动配置
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"
#os.environ['JAVA_HOME'] = 'D:/Java'

conf = SparkConf().setAppName("mapfunc").setMaster("local[*]")
sc = SparkContext(conf=conf)

#map可以对rdd对象的每个元素进行自定义运算
a = [1,2,3,4,5,6]
rdd1 = sc.parallelize(a)

def mult(data):
    return data * 10

rdd1a = rdd1.map(mult)
#rdd1a = rdd1.map(lambda x:x * 10)

#链式调用
rdd2a = rdd1.map(mult).map(lambda x: x+5)
rdd3a = rdd1.map(lambda x: x+5).map(mult)
#从左往右计算

#T -> U代表这个函数要求能够传入一个参数 返回一个值
print(rdd2a.collect())
print(rdd3a.collect())
sc.stop()


