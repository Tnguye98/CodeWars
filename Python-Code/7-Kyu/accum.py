def accum(s):
    c, j = 0, 1
    str = ''
    for i in s:
        c += 1
        str+= i.upper()
        while j != c:
            str += i.lower()
            j += 1
        j = 1
        str +="-"
    str = str[:-1]
    return str


print(accum("abcd"))