def most_occurring_chars(value):
    if not value:
        return None

    counts = {}

    for char in value:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    max_value = 0
    most_occurring_chars_map = {}

    for char, count in sorted(
        counts.iteritems(), key=lambda k, v: (v, k), reverse=True
    ):
        if count > max_value:
            max_value = count

        if count == max_value:
            most_occurring_chars_map[char] = count
        else:
            break

    return most_occurring_chars_map
