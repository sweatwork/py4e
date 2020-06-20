fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File not found:', fname)
    exit()

count = 0
total = 0.0
for line in fhand:
    ipos = line.find('X-DSPAM-Confidence:')
    if ipos == -1:
        continue
    count = count + 1
    xspam = line[ipos:]
    npos = xspam.find(':')
    fnum = float(xspam[npos+1:])
    total = total + fnum
print('Average spam confidence:', total/count)
