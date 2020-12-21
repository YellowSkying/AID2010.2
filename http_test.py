"""
获取http请求和响应
"""
from socket import *

s = socket()
s.bind(("0.0.0.0",9999))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr)

data = c.recv(1024*100)
print(data.decode())

responce = "HTTP/1.1 200 OK\r\n"
responce += "Content-Type:image/jpg\r\n"
responce += "\r\n"
responce = responce.encode()

p = open("wallhaven-0jl25p.png",'rb')
while True:
    data = p.read(1024)
    if not data:
        break
    responce += data

# with open("wallhaven-0jl25p.png",'rb') as p:
#     while True:
#         data = p.read(1024)
#         if not data:
#             break
#         responce += data

c.send(responce)

c.close()
s.close()