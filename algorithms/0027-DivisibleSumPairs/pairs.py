def divisibleSumPairs(numbers, divisor):
    count = 0

    numbers_length = len(numbers)
    for i in range(numbers_length - 1):
        for j in range(i + 1, numbers_length):
            pair_sum = numbers[i] + numbers[j]

            if pair_sum >= divisor and pair_sum % divisor == 0:
                count += 1

    return count
