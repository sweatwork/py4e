# sh = input("Enter hours: ")
# sr = input("Enter rate: ")

try:
    sh = input("Enter hours: ")
    fh = float(sh)

    sr = input("Enter rate: ")
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

print(fh, fr)
pay = fh * fr
print("Pay:", pay)
