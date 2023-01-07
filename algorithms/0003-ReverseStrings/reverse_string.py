def reverse(str):
    if str is None:
        return None

    return "".join([str[i] for i in range(len(str) - 1, -1, -1)])
