def divisors(n):
    count = 0 
    for value in range(1,n+1):
        if (n/value).is_integer() == True:
            count += 1
    return count

print(divisors(12))