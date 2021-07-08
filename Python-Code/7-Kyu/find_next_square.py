def find_next_square(sq):
    isSquare = (sq**(1/2)).is_integer()
    if isSquare == True:
        return int((sq**(1/2)) + 1) ** 2
    return -1

print(find_next_square(121))
print(find_next_square(5169))