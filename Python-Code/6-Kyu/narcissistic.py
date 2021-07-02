def narcissistic( value ):
    x = len(str(value))
    num = 0
    for i in str(value):
        num += int(i)**x
    if num == value:
        return True
    return False




print(narcissistic(153))
print(narcissistic(1938))