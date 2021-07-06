def descending_order(num):
    ans = ""
    num = [x for x in str(num)]
    num.sort(reverse = True)
    for char in num:
        ans+=char
    return int(ans)


print(descending_order(42145))
print(descending_order(145263))