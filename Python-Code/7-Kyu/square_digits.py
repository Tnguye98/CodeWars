def square_digits(num):
    ans = ""
    for i in str(num):
        ans+=str(int(i) * int(i))
    return int(ans)

print(square_digits(33))