def expanded_form(num):
    list = []
    z = len(str(num))-1
    for x in str(num):
        if int(x) == 0:
            z-=1
            continue
        list.append(int(x)*(10**z))
        z-=1
    string = ""
    for i in list:
        string += str(i)
        string += " + "
    return string[:-3]


print(expanded_form(123))
print(expanded_form(9181234))