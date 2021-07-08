def find_it(seq):
    z = [[seq.count(x),x] for x in set(seq)]
    for i in z:
        if (i[0]%2) == 1:
            return i[1]



print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))