import socket
import re

# asking user for a url
url = input('Enter - ')
url_lst = url.split('/')

# creating a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# check for invalid urls
try :
    hostname = url_lst[2]
    # connecting to a host
    mysock.connect((hostname, 80))
except :
    print('Invalid URL')
    quit()

cmd = ('GET '+ url +' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

tmp = ''
while True :
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    tmp += data.decode()
#pos = re.search('\r\n\r\n', tmp).start()
# print(tmp[pos+2:])
print(tmp)
mysock.close()
