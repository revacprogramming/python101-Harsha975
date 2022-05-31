# Network Programming
# https://www.py4e.com/lessons/network
import socket
# socket=socket.socket()
socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('data.pr4e.org', 80))
call='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
socket.send(call)
while True:
    data=socket.recv(1000)
    if len(data)<1:
        break
    print(data.decode())