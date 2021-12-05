# This program aim to determine greater result from multipication of several consturction numbers

def GreaterNumber(number, partition):
    if number%2 == 0:
        a, b = number/2, number/2
        return int(a*b)
    else :
        a = (number-1)*.5
        b = number - a
        return int(a*b)
print(GreaterNumber(11))