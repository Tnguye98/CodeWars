def in_array(array1, array2):
    ans = []
    for i in array1:
        for j in array2:
            if i in j:
                ans.append(i)
                break       
    ans.sort()
    ans = list(dict.fromkeys(ans))
    return ans


a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
