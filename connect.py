#数据库的链接
from pymysql import Connect

conn = Connect(
    host="localhost",
    user="root",
    passwd="123456",
    port=3306

)
print(conn.get_server_info())
#conn.close()#记得关闭

cursor = conn.cursor()
conn.select_db("world")
# cursor.execute('create table pytest(id int);')
cursor.execute('select * from student')

res = cursor.fetchall()
for i in res:
     print(i)


