#打印文件

def printfileinfo(name):
    f = None
    try:
     f = open(name,'r',encoding = 'UTF-8')
     print(f.read())
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()
            #这里判定是为了确定关闭文件的时候文件是正常打开的


# name = input('input:')
# printfileinfo(name)

#追加数据
def fileutil(name,data):
    f = open(name,'a',encoding = 'utf-8')
    f.write(data)
    f.write('\n')
    f.close()
if __name__ =='__main__':
    fileutil(input('文件:'),input('追加的内容：'))

