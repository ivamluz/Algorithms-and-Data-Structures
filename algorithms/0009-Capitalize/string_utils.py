import re


def capitalize(value):
    if not value:
        return value

    alphanum_regex = re.compile(r"\w")

    capitalized_chars_list = []
    idx = 0

    str_chars_list = list(value)
    while idx < len(str_chars_list):
        char = str_chars_list[idx]

        if idx == 0:
            capitalized_chars_list.append(char.upper())
        else:
            previous_char = str_chars_list[idx - 1]
            if re.match(alphanum_regex, previous_char):
                capitalized_chars_list.append(char.lower())
            else:
                capitalized_chars_list.append(char.upper())

        idx += 1

    return "".join(capitalized_chars_list)
