ss = input("Enter score: ")

try :
    fs = float(ss)
except :
    print("Bad score")
    quit()

def computegrade(score):
    if score < 0.0 or score > 1.0 :
        grade = "Bad score"
    else :
        if score >= 0.9 :
            grade = "A"
        elif fs >= 0.8 :
            grade = "B"
        elif fs >= 0.7 :
            grade = "C"
        elif fs >= 0.6 :
            grade = "D"
        elif fs < 0.6 :
            grade = "F"
    return grade

print(computegrade(fs))
