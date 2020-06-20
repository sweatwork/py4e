fname = input('Enter a filename: ')

try :
    fh = open(fname)
except :
    print('File cannot be opened:', fname)
    exit()
day = dict()
for line in fh :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :        # check for an empty line or first word not From
        continue

    day[words[2]] = day.get(words[2], 0) + 1         # idiom
    # if words[2] not in day :
    #     day[words[2]] = 1
    # else :
    #     day[words[2]] += 1
print(day)
