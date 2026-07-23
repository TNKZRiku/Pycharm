from pymysql import connect

conn = connect(
    host="localhost",
    user="root",
    passwd="123456",
    port=3306,
    autocommit=True
    #自动提交 可以省去下文中commit的语句
)
cursor = conn.cursor()
conn.select_db("world")
cursor.execute("insert into student values('10001','zhoujiel','31','nan')")
#写入内容时必须用commit确认
#conn.commit()

conn.close()