def count(word, letter) :
    count = 0
    for c in word:
        if c == 'a':
            count = count + 1
    return count

word = input("Enter a word: ")
letter = input("Enter letter: ")
count = count(word, letter)
print(count)
