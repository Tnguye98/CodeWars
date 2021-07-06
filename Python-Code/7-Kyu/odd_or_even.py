def odd_or_even(arr):
    c = 0
    for i in arr:
        c += i
    if (c%2) == 1:
        return "odd"
    return "even"

print(odd_or_even([0, 1, 4]))
print(odd_or_even([0, -1, -5]))