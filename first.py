import string

fhand = open('romeo-full.txt')
counts = dict()
for line in fhand :
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

# Sort the dictionary by value
lst = list()
for key, value in list(counts.items()) :
    lst.append((value, key))

lst.sort(reverse=True)
print(lst)
for key, val in lst[:10] :
    print(key, val)
