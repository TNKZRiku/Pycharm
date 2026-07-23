#依靠Timeline
from pyecharts.charts import Timeline, Bar
from pyecharts.options import *

bar1 = Bar()
bar1.add_xaxis(['美国','中国','英国'])
bar1.add_yaxis('GDP',[30,10,20],label_opts = LabelOpts(position='right'))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['美国','中国','英国'])
bar2.add_yaxis('GDP',[50,30,40],label_opts = LabelOpts(position='right'))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['美国','中国','英国'])
bar3.add_yaxis('GDP',[70,60,50],label_opts = LabelOpts(position='right'))
bar3.reversal_axis()

timeline = Timeline()#time是一个变量
timeline.add(bar1,'点1')#添加点进时间线
timeline.add(bar2,'点2')
timeline.add(bar3,'点3')

timeline.render('基础时间线柱状图.html')