import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


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
# print(data.decode())

tree = ET.fromstring(data)
comments = tree.find('comments').findall('comment')
count = 0
sum = 0
for comment in comments :
    sum += int(comment.find('count').text)
    count += 1
print('Count:', count)
print('Sum:', sum)
