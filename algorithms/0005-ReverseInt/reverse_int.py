def reverse_int(num):
    if num is None:
        return None

    abs_num = abs(num)
    reversed_num_str = str(abs_num)[::-1]
    reversed_num = int(reversed_num_str) * _sign(num)

    return reversed_num


def _sign(num) -> int:
    if num < 0:
        return -1
    else:
        return 1
