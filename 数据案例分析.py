from filedefine import *
from datadefine import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

textfilerander = TextReader('D:/PyCharm/数据文本/2011.txt')
jsonfilerander = JsonReader('D:/PyCharm/数据文本/2011.json')

jandata:list[Record] = textfilerander.read_data()
febdata:list[Record] = jsonfilerander.read_data()
alldata:list[Record] = jandata + febdata
#print(alldata)
#进行计算
datadict = {}
for record in alldata:
    if record.date in datadict.keys():
        #当前日期已有记录
        datadict[record.date] += record.money

    else:
        datadict[record.date] = record.money

    print(datadict.keys(),datadict[record.date])

#可视化开发
bar = Bar()
bar.add_xaxis(list(datadict.keys()))
bar.add_yaxis('销售额',list(datadict.values()),label_opts = LabelOpts(is_show = False))
bar.set_global_opts(
    title_opts = TitleOpts(title = '每日销售额')
)
bar.render('每日销售额柱状图.html')


