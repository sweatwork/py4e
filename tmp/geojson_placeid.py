import urllib.request, urllib.parse, urllib.error
import json
import ssl


serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
if len(address) < 1:
    print('Bad URL')
    exit()

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
    exit()

# print(json.dumps(js, indent=4))
place_id = js['results'][0]['place_id']
print('Place id', place_id)
