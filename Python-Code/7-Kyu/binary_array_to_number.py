def binary_array_to_number(arr):
  arr = arr[::-1]
  bin, num = 1, 0
  for i in range(len(arr)):
      if arr[i] == 1:
          num += bin
      bin = 2 ** (i+1)
  return num

print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([1, 1, 1, 1]))