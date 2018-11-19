def plus_minus(arr):
  if not arr:
    return [0, 0, 0]

  count = {
    'positives': 0,
    'negatives': 0,
    'zeros': 0
  }

  for i in arr:
    if i > 0:
      count['positives'] += 1
    elif i < 0:
      count['negatives'] += 1
    else:
      count['zeros'] += 1

  length = float(len(arr))

  return [
    round(count['positives'] / length, 6),
    round(count['negatives'] / length, 6),
    round(count['zeros'] / length, 6),
  ]