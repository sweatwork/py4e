fname = input('Enter a file name: ')

try :
    fhand = open(fname)
except :
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From' :
        continue
    addr = words[1]
    counts[addr] = counts.get(addr, 0) + 1          # python idiom
lst = list()
for k, v in counts.items() :
    lst.append((v, k))

lst.sort(reverse=True)

most = list()
for v, k in lst :
    most.append((k, v))
print(most[0])
