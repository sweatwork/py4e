str = 'X-DSPAM-Confidence: 0.8475'

cpos = str.find(':')
print(cpos)
num = str[cpos+1:]  # cpos+2 to get string without space before
print(num)
fnum = float(num)  # float() will truncate the space before 
print(fnum)
