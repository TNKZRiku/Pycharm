import matplotlib.pyplot as plt
import random

#常用功能 figure画布 grid网格线 x/ytick xy轴刻度 x/y legend图例
#title标题 x/ylabel xy轴标签

#额外配置
plt.rcParams['font.sans-serif'] = ['SimHei']

x = [1,2,3,4,5,6,7,8,9,10]
y = [random.randint(0,10) for i in range(10)]
y2 = [random.randint(0,10) for i2 in range(10)]

#设置画布 大小：长，宽
plt.figure(figsize=(10,5))

plt.plot(x,y,label = "城市1")
#重复调用可以生成多个曲线
plt.plot(x,y2,label = "城市2")

plt.title("这是标题",fontsize=20)
#注意 原生不支持中文输入 需要额外配置

plt.xlabel("这里是x轴标签",fontsize=20)
plt.ylabel("这里是y轴标签",fontsize=20)
#如果觉得这里的刻度不够精细 可以直接手动传入
plt.xticks(x)
#也可以通过切片操作实现省略部分刻度

#同理 也可以设定从0开始 但是这时候y的值是无序的 需要额外生成
plt.yticks([i for i in range(0,10+1)])


#网格线部分
plt.grid(linestyle='-.',alpha=0.5)
#        线条样式         透明度


#图例部分
#可以直接传列表 但是如果后续修改也要跟着修改 所以这里用另一种方式
# 上方创建折线的时候一起创建图例
plt.legend(loc="upper left") #这里指定左上角
#这里是可以传入参数的 默认右上角


plt.show()