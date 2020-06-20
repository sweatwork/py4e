from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
counts = list()
for tag in tags :
    counts.extend(tag.contents)

print(len(counts))
sum = 0
for i in counts :
    sum += int(i)
print(sum)
