import string

def is_pangram(s):
    list = []
    for c in s:
        temp = ord(c)
        if temp not in list:
            list.append(temp)
    if len(list) >= 27:
        return True
    return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("racecar"))