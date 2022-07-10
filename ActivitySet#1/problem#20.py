from urllib.request import*
from bs4 import BeautifulSoup
count=0
url=input('enter the url :')
html=urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
for tag in tags:
    count+=int(tag.contents[0])
print(count)