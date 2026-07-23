#制作一个地图

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()#map是一个变量

data = [
    ('北京市',199),
    ('上海市',299),
    ('湖南省',399),
    ('台湾省',499),
    ('广东省',599)
]

map.add('测试地图',data,'china')

#进行全局变量配置
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show = True,
        is_piecewise = True,
        pieces = [
            {'min':1,'max':9,'label':'1-9','color':'#CCFFFF'},
            {'min':10,'max':99,'label':'10-99','color':'#FF6666'},
            {'min':100,'max':999,'label':'100-999','color':'#990033'}
        ]
    )
)


map.render('map.html')#用这个创建HTML文件
