KANGAROO_RESULT_YES = 'YES'
KANGAROO_RESULT_NO = 'NO'

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return KANGAROO_RESULT_NO

    # see https://www.math10.com/en/algebra/arithmetic-progression.html
    steps = float((x2 - x1 + v1 - v2)) / (v1 - v2)

    if steps > 0 and steps.is_integer():
        return KANGAROO_RESULT_YES
    else:
        return KANGAROO_RESULT_NO
