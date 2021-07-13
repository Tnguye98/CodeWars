def dig_pow(n, p = 1):
    listNum = [int(n) for n in str(n)]
    newNum = 0 
    for i in listNum:
        newNum += i ** p
        p+= 1
    if (newNum % n) == 0:
        return newNum / n
    else:
        return -1

print(dig_pow(89))
print(dig_pow(695, 2))