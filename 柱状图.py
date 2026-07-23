#依靠bar模块

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(['中国','美国','英国'])

bar.add_yaxis('GDP',[30,20,10],
              label_opts = LabelOpts(position = 'right')
              )

bar.reversal_axis()#这一行翻转XY轴

bar.render()
