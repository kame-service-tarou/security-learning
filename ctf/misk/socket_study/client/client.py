import socket

class Client:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 7700
        self.socket_make(self.ip, self.port)

    def socket_make(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4,TCP
        #self.s.bind((ip,port)) #必要なし
        #self.s.listen(1) #必要なし
        self.s.connect((ip, port))
        self.s.send(b"Hello") #バイナリ形式で送らないといけない
        data = self.s.recv(1024)
        print(data)
        
client = Client()