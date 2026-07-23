#flatmap用于解除多层嵌套
from pyspark import SparkContext
from pyspark import SparkConf

import os

os.environ['PYSPARK_PYTHON'] = "C:/Users/25162/PyCharmMiscProject/spark/.venv/Scripts/python.exe"
#os.environ['JAVA_HOME'] = 'D:/Java'

conf = SparkConf().setMaster('local[*]').setAppName('flatmapfunc')
sc = SparkContext(conf=conf)

#以下两行运行得到三个字符串列表
#[['tmtk', 'htc', 'mrsm'], ['mtks', 'nji', 'skb'], ['tnkz', 'sryk', 'khbr']]
rdd1 = sc.parallelize(['tmtk htc mrsm','mtks nji skb','tnkz sryk khbr'])
#rdd2 = rdd1.map(lambda x:x.split(' '))

#而以下这一行会消除多层嵌套
#['tmtk', 'htc', 'mrsm', 'mtks', 'nji', 'skb', 'tnkz', 'sryk', 'khbr']
rdd3 = rdd1.flatMap(lambda x:x.split(' '))

print(rdd3.collect())
sc.stop()
