fhand = open('romeo.txt')

final_list = []
for line in fhand :
    words = line.split()
    for word in words :
        if word in final_list :
            continue
        final_list.append(word)
        
final_list.sort()
print(final_list)
