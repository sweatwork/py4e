# modifying the argument
def chop(mod_list) :
    first_elem = 0
    mod_list.remove(mod_list[first_elem])
    last_elem = len(mod_list) - 1
    mod_list.remove(mod_list[last_elem])

# returning a new list 
def middle(new_list) :
    n_list = new_list[1:len(new_list)-1]
    return n_list

s = ['1', '2', '3', '4', '5']
print(s)
chop(s)
print(s)

fruits = ['apple', 'banana', 'orange', 'pineapple']
print(fruits)
f = middle(fruits)
# print(fruits)
print(f)
