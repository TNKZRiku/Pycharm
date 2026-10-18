#matplotlib是一个强大的数据可视化三方库
import matplotlib.pyplot as plt
import random

#手动写入xy数据
x = [1,2,3,4,5,6,7,8,9,10]
y = [random.randint(1,100) for i in range(10)]

#生成折线图
plt.plot(x,y)
#显示图表
plt.show()