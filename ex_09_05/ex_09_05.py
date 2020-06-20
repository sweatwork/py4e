fname = input('Enter a filename: ')

try :
    fh = open(fname)
except :
    print('File cannot be opened:', fname)
    exit()

domain = dict()
for line in fh :
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From' :        # check for an empty line or first word not From
        continue
    dpos = words[1].find('@')
    d = words[1][dpos+1:]
    domain[d] = domain.get(d, 0) + 1

print(domain)
