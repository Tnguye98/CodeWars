def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr, reverse=True):
        return 'yes, descending'
    else: 
        return 'no'



print(is_sorted_and_how([1,2,3,4]))
print(is_sorted_and_how([4,3,2,1]))