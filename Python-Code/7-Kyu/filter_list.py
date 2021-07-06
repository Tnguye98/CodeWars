def filter_list(l):
    newList = []
    for i in l:
        if type(i) == int:
            newList.append(int(i))
    return newList


print(filter_list([1,2,'a','b']))