from DataDefine import DataDefine
import json

class FileReader:
    def dataread(self) -> list[DataDefine]:
        pass

class TextRead(FileReader):
    def __init__(self,path):
        self.path = path

    def dataread(self) -> list[DataDefine]:
        f = open(self.path,'r',encoding="utf-8")
        data_list1 = []
        for line in f.readlines():
            #消除空格和反斜杠
            line = line.strip()
            datalist = line.split(',')
            datadefine = DataDefine(datalist[0],datalist[1],datalist[2],datalist[3])
            data_list1.append(datadefine)

        f.close()
        return data_list1

class JsonRead(FileReader):

    def __init__(self,path):
        self.path = path

    def dataread(self) -> list[DataDefine]:
        f = open(self.path,'r',encoding="utf-8")
        data_list2 = []
        for line in f.readlines():
            print(line)
            #读取到JSON字符串
            json_data = json.loads(line)
            #print(json_data.keys())
            datadefine = DataDefine(json_data['date'],json_data['order_id'],json_data['money'],json_data['province'])
            data_list2.append(datadefine)

        f.close()
        return data_list2



if __name__ == '__main__':
    text = TextRead('D:/李空的下载/数据/1yue.txt')
    json1 = JsonRead('D:/李空的下载/数据/2yue.json')
    list1 = text.dataread()
    list2 = json1.dataread()
    print(list1)
    print(list2)














