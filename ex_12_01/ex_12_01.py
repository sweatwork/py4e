import socket

# asking user for a url
url = input('Enter - ')
url_lst = url.split('/')

# creating a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    hostname = url_lst[2]
    # connecting to a host
    mysock.connect((hostname, 80))
except :
    print('Invalid URL')
    quit()

cmd = ('GET '+ url +' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True :
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print(data.decode(), end='')

mysock.close()
