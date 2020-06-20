# user input
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

# checking input
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error: Enter correct value.")
    quit()

if fh > 40:
    reg = fh * fr          # amount for hours worked
    otp = (fh - 40.0) * (0.5 * fr)  # amount for overtime hours
    pay = reg + otp
else:
    pay = fh * fr

print("Pay:", pay)
