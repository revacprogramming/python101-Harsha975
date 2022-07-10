# Network Programming
# https://www.py4e.com/lessons/network
import socket
# socket=socket.socket()
'''socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('data.pr4e.org', 80))
call='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
socket.send(call)
while True:
    data=socket.recv(1000)
    if len(data)<1:
        break
    print(data.decode())'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
url=input('enter the url- ')
counts=int(input('enter count: '))
position=int(input('enter position: '))
# html=urlopen(url).read()
# soup=BeautifulSoup(html,'html.parser')
# print(soup)
# divs=soup.find('li',class_='reference internal')
# print(divs)
# count=0
# tags = soup('a')
for i in range(counts):
    count=0
    html=urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    # print(count)
    tags = soup('a')
    for tag in tags:
        if count<position:
            # print(tag.get('href'))
            count+=1
            url=tag.get('href')
    print('Retrieving:',url)