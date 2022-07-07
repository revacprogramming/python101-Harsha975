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
'''03'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)