fname = input('Enter file name: ')

try :
    fh = open(fname)
except :
    print("File cannot be opened:", fname)
    exit()

eadd = dict()

for line in fh :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    eadd[words[1]] = eadd.get(words[1], 0) + 1
    # if words[1] not in eadd :
    #     eadd[words[1]] = 1
    # else :
    #     eadd[words[1]] += 1

largest = -1
theword = None
for key, value in eadd.items() :
    if largest < value :
        largest = value
        theword = key

print(theword , largest)
