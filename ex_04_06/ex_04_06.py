# function to calculate pay including overtime
def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate          # amount for hours worked
        otp = (hours - 40.0) * (0.5 * rate)  # amount for overtime hours
        pay = reg + otp
    else:
        pay = hours * rate
    return pay


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

xp = computepay(fh, fr)
print("Pay:", xp)
