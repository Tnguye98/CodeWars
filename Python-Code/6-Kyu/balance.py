def balance(left, right):
    leftPoints = (left.count("!") * 2) + (left.count("?") * 3)
    rightPoints = (right.count("!") * 2) + (right.count("?") * 3)

    if leftPoints > rightPoints:
        return "Left"
    elif leftPoints < rightPoints:
        return "Right"
    return "Balance"


print(balance("!!","??") )
print(balance("!??","?!!"))