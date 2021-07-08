def encode(st):
    x = [c for c in st]
    dic = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
    for n, i in enumerate(x):
        if dic.get(i) != None:
            x[n] = str(dic[i])
    ans = ''.join(x)
    return ans
    
    
def decode(st):
    x = [c for c in st]
    dic = {'1':'a', '2':'e', '3':'i', '4':'o', '5':'u'}
    for n, i in enumerate(x):
        if dic.get(i) != None:
            x[n] = dic[i]
    ans = ''.join(x)
    return ans


print(encode('hello'))
print(encode('How are you today?'))
print(decode('h2ll4'))