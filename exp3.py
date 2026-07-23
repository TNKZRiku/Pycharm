#"D:/李空的下载/数据/rdd案例3.txt"
#目标：1 热门搜索时间段
#     2 热门搜索词
#     3 检索黑马程序员出现频率最高的时间段
#     4 输出为JSON文件

from pyspark import SparkContext
from pyspark import SparkConf
import os
import json

os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"
os.environ['HADOOP_HOME'] = "D:/Hadoop/hadoop-3.0.0"
conf = SparkConf().setAppName("exp3").setMaster('local[*]')
sc = SparkContext(conf=conf)

org_rdd = sc.textFile("D:/李空的下载/数据/rdd案例3.txt")
text_rdd = org_rdd.map(lambda line:line.split("\t"))
# [['21:00:00 1234567890123456 hadoop 3 2 http://www.itcast.cn'], ...
#时间 编号 关键词 数据1 数据2 网址
dict_rdd = text_rdd.flatMap(lambda line:line).map(lambda line:line.split(" "))
#[['21:00:00', '1234567890123456', 'hadoop', '3', '2', 'http://www.itcast.cn'],
time_rdd = dict_rdd.map(lambda x:(x[0],1))
time_res_rdd = time_rdd.reduceByKey(lambda x,y:x+y)
#[('21:00:00', 10), ('21:05:00', 3)]
time_sort_rdd = time_res_rdd.sortBy(lambda x:x[1],ascending=False)
#print(time_sort_rdd.collect())
time_max_rdd = time_sort_rdd.take(1)

word_rdd = dict_rdd.map(lambda x:(x[2],1))
word_add_rdd = word_rdd.reduceByKey(lambda x,y:x+y)
word_sort_rdd = word_add_rdd.sortBy(lambda x:x[1],ascending=False)
word_max_rdd = word_sort_rdd.take(1)

funl_rdd = dict_rdd.map(lambda x:(x[0],x[2]))
funl_time_rdd = funl_rdd.map(lambda x:(x[0],1))
funl_add_rdd = funl_time_rdd.reduceByKey(lambda x,y:x+y)
funl_sort_rdd = funl_time_rdd.sortBy(lambda x:x[1],ascending=False)
funl_max_rdd = funl_sort_rdd.take(1)

print('最热门的搜索时间段是{}，出现了{}次搜索'.format(time_max_rdd[0][0],time_max_rdd[0][1]))
print('最热门的搜索词是{}，出现了{}次'.format(word_max_rdd[0][0],word_max_rdd[0][1]))
print('‘黑马程序员’最热门的搜索时间段是{}，出现了{}次'.format(funl_max_rdd[0][0],funl_max_rdd[0][1]))

all_rdd = sc.parallelize([time_max_rdd,word_max_rdd,funl_max_rdd])
all_rdd.saveAsTextFile("D:/李空的下载/导出的数据/exp3")
all_rdd_list = [{time_max_rdd[0][0]:time_max_rdd[0][1]},{word_max_rdd[0][0]:word_max_rdd[0][1]},{funl_max_rdd[0][0]:funl_max_rdd[0][1]}]
with open("D:/李空的下载/导出的数据/exp3cl.json", "w") as fp:
    json.dump(all_rdd_list, fp)