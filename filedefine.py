#文件的类定义
import json

from datadefine import Record
#定义一个顶层类
class FileReader:
    def read_data(self)->list[Record]:
        '''读到的每一条对象都转化为record对象 封装到list内返回'''
        pass

class TextReader:
    def __init__(self,path):
        self.path = path
        #记录文件路径
    #复写
    def read_data(self)->list[Record]:
        f = open(self.path,'r',encoding='utf-8')
        recordlist = []
        for line in f.readlines():
            line = line.strip()
            datalist = line.split(',')
            record = Record(datalist[0],datalist[1],int(datalist[2]),datalist[3])
            recordlist.append(record)
        f.close()
        return recordlist


class JsonReader:
    def __init__(self,path):
        self.path = path
    def read_data(self)->list[Record]:
        f = open(self.path,'r',encoding='utf-8')
        recordlist = []
        for line in f.readlines():
            datadict = json.loads(line)
            record = Record(datadict['date'],datadict['order_id'],datadict['money'],datadict['province'])
            recordlist.append(record)
        f.close()
        return recordlist

if __name__ == '__main__':
    textfilerander = TextReader('D:/PyCharm/数据文本/2011.txt')
    jsonfilerander = JsonReader('D:/PyCharm/数据文本/2011.json')

    list1 = textfilerander.read_data()
    list2 = jsonfilerander.read_data()

    for l in list1:
        print(l)
    for r in list2:
        print(r)