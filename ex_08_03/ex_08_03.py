fname = input('Enter filename: ')

try:
    fhand = open(fname)
except:
    print("File not found:", fname)
    exit()

count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' : continue
    print(words[2])
