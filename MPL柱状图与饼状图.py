#在实际应用中 一个画布可以同时创建多个图表
#subplots函数 其中行数nrows 列数ncols 尺寸figsize 分辨率dpi
import random

from matplotlib import pyplot as plt
from matplotlib.axes import Axes

plt.rcParams['font.sans-serif']=['SimHei']

#创建返回的数组 通过索引操作不同的图
figure,axes = plt.subplots(1,2,dpi=200)
#创建时返回为元组类型 第一个是画布对象

#这里的变量是未知的类型 需要手动加上类型注解才会有提示
axes1 : Axes= axes[0]
axes2 : Axes= axes[1]


axes1.set_title("这是一号标题，石油储备",fontsize=14)
countrys = ["中国",'美国',"俄罗斯",'沙特',"阿拉伯",'日本']
values = [random.randint(0,100) for _ in range(6)]
#生成柱状图 多种自定义参数              颜色        宽度
axes1.bar(countrys,values,color = 'green',width=0.5)
axes1.set_xlabel('国家')
axes1.set_ylabel('石油储备')
axes1.grid(True,linestyle='--',alpha=0.3)

#下面是饼状图
countrys2 = ['中国','美国','俄罗斯','印度','法国','英国','日本']
values2 = [random.randint(10,100) for _ in range(7)]

axes2.pie(values2,labels=countrys2,autopct='%1.1f%%')
#                         这个是总位数 不足补空格↑  ↑  ↑这两个百分号用来转义
#                                 这是小数位数限制 ↑

axes2.set_title("人口占比",fontsize=14,color='red')
axes2.legend(loc='lower center',ncol=5,fontsize=6,bbox_to_anchor=(0.5, -0.2))
#                           每列的限制↑                          图例位置↑

#这张图其实是可以保存的
plt.savefig("data/pie,col.jpg")

plt.show()
