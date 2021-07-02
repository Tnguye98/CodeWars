def getCount(inputStr):
    num_vowels = 0
    vowels = ["a","e","i","o","u"]
    inputStr.lower()
    list(inputStr)
    for i in inputStr:
        if i in vowels:
            num_vowels += 1
    return num_vowels


print(getCount("Hello"))
print(getCount("aeiou"))