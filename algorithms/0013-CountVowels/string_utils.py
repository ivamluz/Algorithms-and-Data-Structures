import re

def count_vowels(str):
  if not str:
    return 0

  cleaned_str = re.sub(
    r"[^aeiouAEIOU]", 
    '', 
    str
  )

  unique_vowels = set(cleaned_str.lower())

  return len(unique_vowels)