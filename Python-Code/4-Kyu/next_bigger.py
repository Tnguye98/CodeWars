def next_bigger(n):
    listNum = [num for num in str(n)]
    biggestNum = int("".join(sorted(listNum, reverse = True)))
    copyN = n
    while copyN <= biggestNum:
        copyN += 1
        copyList = [num for num in str(copyN)]
        if sorted(copyList) == sorted(listNum):
            return copyN
    return -1
print(next_bigger(144))