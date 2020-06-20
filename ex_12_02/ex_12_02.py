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

count = 0
while True :
    data = mysock.recv(512)
    dl = len(data)
    if dl < 1 :
        break
    count += dl
    if count <= 3000 :
        print(data.decode(), end='')

print('\nTotal characters: ', count)
mysock.close()
