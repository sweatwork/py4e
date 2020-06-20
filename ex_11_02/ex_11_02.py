import re

fname = input('Enter file: ')

try :
    hand = open(fname)
except :
    print('File cannot be opened')
    quit()

lst = list()
for line in hand :
    line = line.rstrip()
    n = re.findall('New Revision: ([0-9]+)', line)
    if len(n) > 0 :
        lst.extend(n)
# print(lst)
count = len(lst)
sum = 0
for i in lst :
    sum += int(i)
print(sum//count)
