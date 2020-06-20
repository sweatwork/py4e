fh = open('words.txt')

word_dict = dict()
for line in fh :
    line = line.rstrip()
    words = line.split()
    for w in words :
        word_dict[w] = ''
    print(word_dict)

s = input('Enter a word: ')
if s in word_dict :
    print(s, 'is in the dictionary')
else:
    print(s, 'is not in the dictionary')
