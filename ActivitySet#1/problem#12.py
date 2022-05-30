# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
d=0
f=open('http://py4e-data.dr-chuck.net/regex_sum_1550206.txt','r')
for line in f:
    g=re.findall('\d+',line)
    if g!=None:
        for i in g:
            d+=int(i)
print(d)