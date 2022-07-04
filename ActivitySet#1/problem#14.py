# Using Web Services
# https://www.py4e.com/lessons/servces
import urllib.request
import xml.etree.ElementTree as et
from urllib.request import*
url=input("enter the url :")
# data=urllib.request.urlopen(url)
tree=et.fromstring(data).