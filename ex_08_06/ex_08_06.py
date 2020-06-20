numbers = []

while True:
    n = input('Enter a number: ')
    if n == 'done' : break
    if n == '' : continue
    n = float(n)
    numbers.append(n)
print('Maximum:', max(numbers))
print('Minimum:', min(numbers))
