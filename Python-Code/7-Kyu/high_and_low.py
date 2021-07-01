def high_and_low(numbers):

    numbers = numbers.split(" ")
    max, min = int(numbers[0]), int(numbers[0])
    for i in numbers:
        if (int(i) > max):
            max = int(i)
        if (int(i) < min):
            min = int(i)
    numbers = str(max) + " " + str(min)
    return numbers





print(high_and_low("1 2 3 4 5"))