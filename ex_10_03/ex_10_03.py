import string

fname = input('Enter a file name: ')
if fname == "" :
    fname = 'mbox-short.txt'

try :
    fhand = open(fname)
except :
    print('File cannot be opened')
    exit()

counts = dict()
for line in fhand :
    line = line.strip()
    line = line.translate(str.maketrans("", "", string.punctuation+string.digits))
    line = line.replace(' ', '')
    line = line.lower()
    words = list(line)
    for letter in words :
        counts[letter] = counts.get(letter, 0) + 1
lst = list()
for k, v in counts.items() :
    lst.append((v, k))
lst.sort(reverse=True)
for k, v in lst :
    print(v, k)
