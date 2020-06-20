fname = input('Enter a file name: ')

try :
    fhand = open(fname)
except :
    print('File cannot be opened or not found.')
    exit()

hours = dict()
for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != 'From' :
        continue
    time = words[5]
    hour = time[:2]
    hours[hour] = hours.get(hour, 0) + 1

lst = list()
for k, v in hours.items() :
    lst.append((k, v))

lst.sort()

for k,v in lst :
    print(k, v)
