def count_deaf_rats(town):
    locationOfPiper = 0
    for location in range(len(town)):
        if town[location] == 'P':
            locationOfPiper = location
    leftSide, rightSide = town[:locationOfPiper], town[(locationOfPiper + 1):]
    
    leftSideList, rightSideList = [], []
    location = 0
    while location != len(leftSide):
        if leftSide[location] == 'O' or leftSide[location] == '~':
            leftSideList.append(leftSide[location:location+2])
            location += 1
        location += 1
    location = 0
    while location != len(rightSide):
        if rightSide[location] == 'O' or rightSide[location] == '~':
            rightSideList.append(rightSide[location:location+2])
            location += 1
        location += 1
    
    ans = 0
    for i in leftSideList:
        if i == "O~":
            ans += 1
    for i in rightSideList:
        if i == "~O":
            ans += 1
    return ans


print(count_deaf_rats("P O~ O~ ~O O~"))
print(count_deaf_rats("~O~O~O~OP~O~OO~"))