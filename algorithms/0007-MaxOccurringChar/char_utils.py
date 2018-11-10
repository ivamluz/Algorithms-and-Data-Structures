def most_occurring_chars(str):
  if not str:
    return None

  counts = {}
  for char in str:
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1

  max = 0
  most_occurring_chars_map = {}
  for char, count in sorted(counts.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    if count > max:
      max = count

    if (count == max):
      most_occurring_chars_map[char] = count
    else:
      break

  return most_occurring_chars_map