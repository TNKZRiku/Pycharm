#socket用于完成简单的客户端和服务端开发
#服务端用来接收客户端数据 并给出回复
import socket
#创建类对象
socket_server = socket.socket()
#绑定端口和ip
socket_server.bind(('localhost',int('0721',10)))
#监听目标（1个）
socket_server.listen(1)
#接下来调用accept方法会返回两个值 链接对象和地址
# result = socket_server.accept()
# conn = result[0]
# addr = result[1]
#简化写法
conn,addr = socket_server.accept()
#accept如果没有接收到值 会停滞不前
print('接收成功 用户地址为{}'.format(addr))

#接收信息 需要注意的是此处调用链接对象conn，而且需要编码解码
data = conn.recv(1024).decode('utf-8')
print(data)
#发送信息
msg = input('回复：').encode('utf-8')
conn.send(msg)
conn.close()
#此处可以先不关闭 继续接收内容
socket_server.close()


