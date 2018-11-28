KANGOROO_RESULT_YES = 'YES'
KANGOROO_RESULT_NO = 'NO'

def kangaroo(x1, v1, x2, v2):
    arithmetic_progression = lambda first, difference, n: first + (n - 1) * difference

    for i in range(2, 10000):
        kangaroo1_position = arithmetic_progression(x1, v1, i)
        kangaroo2_position = arithmetic_progression(x2, v2, i)

        if kangaroo1_position == kangaroo2_position:
            return 'YES'

    return 'NO'
