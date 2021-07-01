def find_uniq(arr):
    firstVar,uni, c = arr[0], 0, 0
    c = 0
    for i in arr:
      if firstVar == i:
          pass
      else:
          uni = i
          c += 1
    if c == 1:
        return uni
    else:
        return firstVar

