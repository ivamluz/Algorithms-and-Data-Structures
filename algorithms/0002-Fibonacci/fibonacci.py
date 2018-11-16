# TODO: Memoize next_fibonacci_number function
def next_fibonacci_number(position):
  if position <= 1:
    return position

  return next_fibonacci_number(position - 1) + next_fibonacci_number(position - 2)


def build_fibonacci_sequence_up_to(max_value):
  if max_value <= 0:
    return None

  position = 0
  next_value = 0

  sequence = []
  while next_value <= max_value:
    next_value = next_fibonacci_number(position)

    if (next_value <= max_value):
      sequence.append(next_value)
    
    position += 1

  return sequence