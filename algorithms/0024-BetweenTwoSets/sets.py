def getTotalX(a, b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    limit = max(sorted_a[len(sorted_a) - 1], sorted_b[0])

    count = 0
    for i in range(1, limit + 1):
        is_match = True

        for a_item in a:
            if i % a_item > 0:
                is_match = False
                break

        for b_item in b:
            if b_item % i > 0:
                is_match = False
                break

        if is_match:
            count += 1   

    return count