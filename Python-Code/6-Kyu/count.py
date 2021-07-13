def count(string):
    dictionaryString = {}
    for i in string:
        if dictionaryString.get(i) == None:
            dictionaryString[i] = 1
        else:
            dictionaryString[i] += 1
    return dictionaryString


print(count("ababalasldfnasjnc"))