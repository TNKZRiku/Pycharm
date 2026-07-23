#共有4种可以返回为py对象的func
# collect reduce count take

from pyspark import SparkContext
from pyspark import SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"

conf = SparkConf().setAppName("fliterfunc").setMaster('local[*]')
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1,2,3,4,5,6])
#collect用于直接把rdd对象的全部内容转换为一个列表
text1 = rdd1.collect()
print('collect:',text1)

#reduce用于对rdd内的所有内容进行指定计算并返回一个数值
text2 = rdd1.reduce(lambda a,b : a + b)
print('reduce:',text2)

#count会返回rdd内元素总数的值
text3 = rdd1.count()
print('count:',text3)

#take用于返回前n个元素
text4 = rdd1.take(3)
print('take:',text4)
