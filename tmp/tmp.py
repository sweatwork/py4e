def wrap(string, max_width):
    new_str = ''
    l = len(string)
    p = max_width
    for i in range(0, l, max_width) :
        new_str += string[i:p] + '\n'
        p += max_width
    return new_str.strip()

print(wrap('bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd', 9))
