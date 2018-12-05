def findDigits(number):
    # one liner
    # return sum(map(lambda x: 1 if int(x) > 0 and number % int(x) == 0 else 0, str(number)))

    count = 0
    for digit in [int(d) for d in str(number)]:
        if digit > 0 and number % digit == 0:
            count += 1

    return count