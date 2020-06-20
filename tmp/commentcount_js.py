import urllib.request
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    print('Bad URL')
    exit()

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info['comments']
count = 0
sum = 0
for u in comments :
    sum += u['count']
    count += 1
print('Count:', count)
print('Sum:', sum)
