import socket

HOST = "127.0.0.1"
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.python.org", 80))