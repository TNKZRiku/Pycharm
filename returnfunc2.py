#rdd内容也可以直接导出为文件
#但是需要配置Hadoop依赖
#saveAsTextFlie

from pyspark import SparkContext
from pyspark import SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"
os.environ['HADOOP_HOME'] = "D:/Hadoop/hadoop-3.0.0"

conf = SparkConf().setAppName("fliterfunc").setMaster('local[*]')
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize((1,2,3,4,5,6,7,8,9))
rdd2 = sc.parallelize({1:'hello',2:'no hello'})
rdd3 = sc.parallelize([[1,2],[3,4],[5,6],[7,8],[9,9]])

#需要注意的是导出的文件夹必须是全新的
rdd1.saveAsTextFile("D:/李空的下载/导出的数据/wjj1")
rdd2.saveAsTextFile("D:/李空的下载/导出的数据/wjj2")
rdd3.saveAsTextFile("D:/李空的下载/导出的数据/wjj3")