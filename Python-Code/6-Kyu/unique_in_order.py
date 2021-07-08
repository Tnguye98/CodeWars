def unique_in_order(iterable):
    list = []
    try:
      list = [iterable[0]]
    except:
      return list
    for c in iterable:
        if c != list[-1]:
            list.append(c)
    return list



print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1,2,2,3,3]))