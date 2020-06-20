import re

rex = input('Enter a regular expression: ')

hand = open('mbox.txt')

count = 0
for line in hand :
    line = line.rstrip()
    if re.search(rex, line) :
        print(line)
        count += 1
print('mbox-txt had', count, 'lines that matched', rex)
