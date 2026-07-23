#基础折线图
from pip._internal.resolution import legacy
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

line = Line()#此处line是折线图 本质上是一个变量

line.add_xaxis(['China','America','England'])
line.add_yaxis('GDP',[30,20,10])

line.set_global_opts(
    title_opts=TitleOpts(title='GDP展示',pos_left='center'),
    #这里pos是位置
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts = ToolboxOpts(is_show=True),
    visualmap_opts = VisualMapOpts(is_show=True)
)

#render可以把数据生成图表
line.render()

