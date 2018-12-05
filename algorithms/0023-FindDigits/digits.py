def findDigits(number):
    # one liner
    # return sum(map(lambda x: 1 if int(x) > 0 and number % int(x) == 0 else 0, str(number)))

    digits = [int(x) for x in str(number)]
    
    count = 0
    for digit in digits:
        if digit > 0 and number % digit == 0:
            count += 1

    return count