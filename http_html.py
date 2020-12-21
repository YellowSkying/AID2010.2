"""
web 服务程序实现
"""
from socket import *
from select import *

class Responce:
    @staticmethod
    def solve_connect(sock):
        connfd, addr = sock.accept()
        print("Connect from",addr)
        connfd.setblocking(False)
        return connfd

    @staticmethod
    def handle(connfd):
        data = connfd.recv(1024*100).decode()
        request_line = data.split('/r/n')[0]
        request = request_line.split(' ')[1]
        print(request)



class HtmlServer:
    def __init__(self,host="0.0.0.0",port=8888,html=""):
        self.HOST = host
        self.PORT = port
        self.html = html
        self.ADDR = (self.HOST,self.PORT)
        self.tcp_socket = self.create_socket(self.ADDR)

    def create_socket(self, ADDR):
        tcp_socket = socket(AF_INET,SOCK_STREAM)
        tcp_socket.bind(ADDR)
        tcp_socket.setblocking(False) # 将IO设置为非阻塞IO，与IO多路复用配套使用
        return tcp_socket

    def IO_concurrent(self):
        map = {self.tcp_socket.fileno():self.tcp_socket}
        ep = epoll()
        ep.register(self.tcp_socket,EPOLLIN|EPOLLERR)
        while True:
            events = ep.poll()
            for fd,event in events:
                if event == EPOLLIN:
                    if fd == self.tcp_socket.fileno():
                        connfd = Responce.solve_connect(map[fd])
                        map[connfd.fileno()] = connfd
                    else:
                        Responce.handle(map[fd])




    def start(self):
        print("Start listening")
        self.tcp_socket.listen(10)
        self.IO_concurrent()




if __name__ == '__main__':
    httpd = HtmlServer(host="0.0.0.0",port=8777,html="./static")
    httpd.start()