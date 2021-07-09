def two_sum(numbers, target):
    cache = []
    for i in range(len(numbers)):
        if target - numbers[i] in cache:
            return [numbers.index(target - numbers[i]), i]
        cache.append(numbers[i])



print(two_sum([1,2,3], 4))