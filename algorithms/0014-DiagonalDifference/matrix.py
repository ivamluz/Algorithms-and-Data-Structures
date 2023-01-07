def diagonal_difference(arr):
    if not arr:
        return 0

    sum = 0

    size = len(arr[0])
    for i in range(0, size):
        sum += arr[i][i] - arr[i][size - i - 1]

    return abs(sum)
