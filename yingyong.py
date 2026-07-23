# creat table orders(
#     date data,
#     id varchar(255),
#     money int,
#     province varchar(10)
# )

import fun_fileread
from pymysql import Connect

textfilereader = fun_fileread.TextRead("D:/李空的下载/数据/1yue.txt")
jsonfilereader = fun_fileread.JsonRead("D:/李空的下载/数据/2yue.txt")
yue1 = textfilereader.dataread()
yue2 = jsonfilereader.dataread()

alldata = yue1 + yue2

###############################

conn = Connect(

    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "123456",
    autocommit = True
)

cursor = conn.cursor()
conn.select_db('pymysql')

for data in alldata:
    sql = ("insert into sellorders(date,order_id,money,province) "
           "values('{}','{}',{},'{}')").format(data.data,data.orderid,data.money,data.province)

    cursor.execute(sql)

conn.close()