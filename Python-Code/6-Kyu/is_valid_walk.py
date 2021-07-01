def is_valid_walk(walk):
    n, e , c = 0, 0, 0
    for i in walk:
        if i == 'n' or i == 'e':
            n+=1
        if i == 's' or i =='w':
            n-=1
        c +=1
    if (n == 0) and (e == 0) and (c == 10):
        return True
    else:
        return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))