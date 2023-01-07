def birthday(numbers, day, month):
    expected_sum = day
    expected_length = month

    numbers_length = len(numbers)

    if numbers_length == 1 and numbers[0] == expected_sum:
        return 1

    possibilities = 0
    for i in range(numbers_length - expected_length + 1):
        current_sum = numbers[i]
        current_length = 1

        for j in range(i + 1, i + expected_length):
            current_length += 1
            current_sum += numbers[j]

            if current_sum > expected_sum:
                break

            if current_length == expected_length and current_sum == expected_sum:
                possibilities += 1

    return possibilities
