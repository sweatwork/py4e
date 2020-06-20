fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File not found:', fname)
    exit()

# Approach 1: Convert each line individually,
# good way if low on memory
for line in fhand:
    line = line.rstrip()
    print(line.upper())

# Approach 2: Read the file as one whole chunk of string,
# use when file is small or enough memory to store it as
# one whole chunk
# cfile = fhand.read().upper()
# print(cfile)
