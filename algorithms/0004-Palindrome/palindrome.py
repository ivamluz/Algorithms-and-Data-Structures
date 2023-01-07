import re


def is_palindrome(str):
    if str is None:
        return False

    cleanedStr = re.sub(r"[^a-z0-9]", "", str.lower())

    return cleanedStr == cleanedStr[::-1]
