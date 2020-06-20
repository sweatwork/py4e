from urllib.request import urlopen

# asking user for a url
url = input('Enter - ')

fhand = urlopen(url)
count = 0
for line in fhand :
    count += len(line)
    if count < 3000 :
        print(line.decode().strip())

print('\nTotal characters: ', count)
