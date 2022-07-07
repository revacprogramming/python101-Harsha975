# Using Web Services
# https://www.py4e.com/lessons/servces
'''01'''
import urllib.request
import xml.etree.ElementTree as et
fh=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1550210.xml')
data=fh.read()
tree=et.fromstring(data)
lst=tree.findall('comments/comment') 
sum=0
for items in lst:
    num=int(items.find('.//count').text)
    sum+=num

print(sum)
'''02'''
from urllib.request import urlopen
import json
url='http://py4e-data.dr-chuck.net/comments_1550211.json'
jsFile = urlopen(url)
data =json.loads(jsFile.read())
sum=0
for i in data['comments']:
    sum+=i['count']
print(sum)