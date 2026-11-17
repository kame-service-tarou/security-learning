import socket
import string

host = "34.170.146.252"
port = 62655


class MySocket:
    """説明用のクラス
      - 効率よりも分かりやすさを優先したコード
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while True:
            chunk = self.sock.recv(2048)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            data = b''.join(chunks)
            if b'Input: ' in data:
                data = data.replace(b'Input: ', b'')
                break
        return data
# base64の文字の候補

client = MySocket()
client.connect(host, port)

base64 = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + '+/')

known = b'QWxwYWNhe'
response = client.myreceive()
print(response)
for x in base64:
    msg = known + bytes([0x20]) + b'\n'
    client.mysend(msg)
    response = client.myreceive()
    print(x, repr(response))