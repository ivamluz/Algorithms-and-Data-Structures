def findDigits(number):
    digits = [int(x) for x in str(number)]
    
    count = 0
    for digit in digits:
        if digit == 0:
            continue

        if number % digit == 0:
            count += 1

    return count