#统计前三百名电影的
#每年电影上映数量折线图
#不同类型电影的柱状图
#不同语言电影的柱状图
#统计评分的比例的饼状图

import pandas as pd
import re
from matplotlib import pyplot as plt
from collections import Counter
from mpl_toolkits.axes_grid1.mpl_axes import Axes

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

#借助pandas导入数据
df = pd.read_csv(filepath_or_buffer='D:/李空的下载/导出的数据/movie/movie_info4.csv',encoding='gbk')

#制作折线图
scores_list = df["发行日期"]
scores_list_sorted = scores_list.sort_values()
scores_list_sorted_years = []
years = []
for year in scores_list_sorted:
    scores_list_sorted_years.append(year[:4:])
    if year not in years:
        years.append(year)
count = Counter(scores_list_sorted_years)
#print(count)#:dict {years:counts}
x1 = []
y1 = []
for year in count:
    x1.append(year)
    y1.append(count[year])

#制作不同类型的饼状图

#我没写类型 跳过了

#制作不同语言比例的饼状图

#语言我也没写 跳过了

#跳过太多也不好 这里补充成不同时长吧
#120分钟以下 150分钟 180分钟以上
times_original_list = df["时长"]
times_list = []
times_finally_list = []
count_dict = {}
for time in times_original_list:
    if time:
        times_list.extend((re.findall(r'\d+', time)))
for time in times_list:
    times_finally_list.append(int(time))
for time in times_finally_list:
    if time < 120:
        count_dict['120'] = 1 if '120' not in count_dict else count_dict['120'] + 1
    elif 120 <= time <150:
        count_dict['150'] = 1 if '150' not in count_dict else count_dict['150'] + 1
    elif 150 <= time <180:
        count_dict['180'] = 1 if '180' not in count_dict else count_dict['180'] + 1
    else:
        count_dict['180+'] = 1 if '240' not in count_dict else count_dict['180+'] + 1
#{'150': 35, '180': 5, '120': 55}
x2 = list(count_dict.keys())
y2 = list(count_dict.values())



#制作评分的柱状图 其实评分占比不适合用柱状图 这里是为了练习柱状图
scoress_original_list = df['评分']
scoress_dict = {}

for score in scoress_original_list:
    if score.strip():
        if int(score.strip()) < 70 :
            scoress_dict['70-'] = 1 if '70-' not in scoress_dict else scoress_dict['70-'] + 1
        elif 70 <= int(score.strip()) < 75 :
            scoress_dict['75'] = 1 if '75' not in scoress_dict else scoress_dict['75'] + 1
        elif 75 <= int(score.strip()) < 80:
            scoress_dict['80'] = 1 if '80' not in scoress_dict else scoress_dict['80'] + 1
        elif 80 <= int(score.strip()) < 85:
            scoress_dict['85'] = 1 if '85' not in scoress_dict else scoress_dict['85'] + 1
        else:
            scoress_dict['85+'] = 1 if '85+' not in scoress_dict else scoress_dict['85+'] + 1
#{'70': 45, '80': 15, '60': 35}
x3 = list(scoress_dict.keys())
y3 = list(scoress_dict.values())


#创建画布
plt.subplots(nrows=2,ncols=2,figsize=(10,6),dpi=200)


ax1 : Axes= plt.subplot(2,2,1)
ax1.set_title('各年份发行数量折线图')
ax1.plot(x1,y1)
ax1.set_xlabel('年份')
ax1.set_xticks(x1)
ax1.set_ylabel('发行数量')
ax1.set_yticks([i for i in range(1-1,100+1-1,20)])


ax2 :Axes= plt.subplot(2,2,2)
ax2.set_title('时长占比饼状图')
ax2.pie(y2,labels=x2,autopct='%1.1f%%')
ax2.legend(bbox_to_anchor=(0.85, 0.6))


ax3 : Axes= plt.subplot(2,2,(3,4))
for a in list(ax3.figure.axes):
    if a is not ax3 and not a.get_title() and not a.get_xlabel():
        a.remove()
ax3.set_title('评分情况柱状图',x=0.6)
ax3.bar(x3,y3,color='green')
ax3.set_xlabel('评分')
ax3.set_xticks(x3)
ax3.set_ylabel('数量')
ax3.set_yticks([i for i in range(1-1,60+1-1,10)])

print("当前 figure 的轴数量:", len(ax3.figure.axes))
print("所有轴:", ax3.figure.axes)

plt.tight_layout()
plt.show()














