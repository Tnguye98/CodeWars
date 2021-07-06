def get_sum(a,b):
    if b < a:
        a, b = b, a
    x = 0
    for i in range(a,b+1):
        x += i
    return x

print(get_sum(1, 2))
print(get_sum(-1, 2))