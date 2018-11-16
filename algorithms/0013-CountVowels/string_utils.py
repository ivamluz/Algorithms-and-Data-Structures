import re

def count_vowels(str):
  if not str:
    return 0

  cleaned_str = re.sub(
    r"[^aeiouAEIOU]", 
    '', 
    str
  )

  return len(cleaned_str)