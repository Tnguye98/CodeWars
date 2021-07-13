def lowest_product(input):
    if len(input) < 4:
        return "Number is too small"
    currentSmallest = int(input[0]) * int(input[1]) * int(input[2]) * int(input[3])
    for numLoc in range(len(input) - 3):
        if currentSmallest > (int(input[numLoc]) * int(input[numLoc + 1]) * int(input[numLoc + 2]) * int(input[numLoc + 3])):
            currentSmallest = (int(input[numLoc]) * int(input[numLoc + 1]) * int(input[numLoc + 2]) * int(input[numLoc + 3]))
    return currentSmallest


print(lowest_product("123456789"))