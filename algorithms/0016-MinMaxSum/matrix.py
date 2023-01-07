def min_max_sum(values):
    if not values:
        return (0, 0)

    sorted_values = sorted(values)

    min = sum(sorted_values[0:4])
    max = sum(sorted_values[1:5])

    return (min, max)
