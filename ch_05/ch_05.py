# Find the largest number
largest_num = -1
print("Before", largest_num)
for num in [3, 41, 12, 9, 74, 6]:
    if num > largest_num:
        largest_num = num
    print(largest_num, num)
print("After", largest_num) 
