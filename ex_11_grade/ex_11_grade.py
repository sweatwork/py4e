import re


fname = input('Enter file: ')
if len(fname) < 1 :
    fname = 'regex_sum_378685.txt'

hand = open(fname)
sum = 0
for line in hand :
    line = line.rstrip()
    n = re.findall('[0-9]+', line)
    for i in n :
        sum += int(i)
print(sum)

# A redacted version of two-line version of this program using list comprehension
# print( sum([int(i) for i in re.findall('[0-9]+', hand.read())]))
