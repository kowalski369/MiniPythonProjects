# this program checks that the given number is armstrong number or not.

def isarmstrong(*n):
    number = list(n)
    val = 0
    digit = ""
    for i in number:
        val = (i**len(n)) + val
        digit = str(i) + digit
    digit = digit[::-1]

    if val == int(digit):
        return True
    else:
        return False

print(isarmstrong(3,7,1))