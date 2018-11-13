def steps(size):
  if size <= 0:
    raise ValueError('Size should be greather than 0.')

  steps = ""
  for row in range(1, size + 1):
    spaces_size = size - row
    
    steps += ('#' * row) + (' ' * spaces_size)

    if row < size:
      steps += "\n"

  return steps