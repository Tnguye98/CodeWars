def find_short(s):
    s = s.split()
    l = len(s[0])
    for i in s:
        if l > len(i):
            l = len(i)
    return l 

print(find_short("Hello my name is Joe"))
print(find_short("long long long long ss"))