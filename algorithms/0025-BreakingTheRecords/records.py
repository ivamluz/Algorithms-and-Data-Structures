def breakingRecords(scores):
    if len(scores) == 1:
        return (0, 0)

    highest_breaks = 0
    lowest_breaks = 0

    highest = scores[0]
    lowest = scores[0]

    for i in range(1, len(scores)):
        score = scores[i]

        if score > highest:
            highest_breaks += 1
            highest = score

        if score < lowest:
            lowest_breaks += 1
            lowest = score

    return (highest_breaks, lowest_breaks)
