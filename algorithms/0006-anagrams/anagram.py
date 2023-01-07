def is_anagram(str1, str2):
    if not str1:
        return False

    if not str2:
        return False

    if len(str1) != len(str2):
        return False

    first_str_chars = {}
    second_str_chars = {}

    for i in range(len(str1)):
        char = str1[i].lower()
        if char in first_str_chars:
            first_str_chars[char] += 1
        else:
            first_str_chars[char] = 1

        char = str2[i].lower()
        if char in second_str_chars:
            second_str_chars[char] += 1
        else:
            second_str_chars[char] = 1

    return first_str_chars == second_str_chars
