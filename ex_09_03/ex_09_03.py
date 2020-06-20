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
    eadd[words[1]] = eadd.get(words[1], 0) + 1          # idiom 
    # if words[1] not in eadd :
    #     eadd[words[1]] = 1
    # else :
    #     eadd[words[1]] += 1

print(eadd)
