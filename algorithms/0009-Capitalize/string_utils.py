import re

def capitalize(str):
  if not str:
    return str

  alphanum_regex = re.compile("\w")

  capitalized_chars_list = []
  idx = 0

  str_chars_list = list(str)
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
