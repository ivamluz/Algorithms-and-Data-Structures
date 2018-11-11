def chunk(arr, size):
  if size <= 0:
    raise ValueError('Size shoudl be greather than 0.')

  if not arr:
    return []

  start = 0
  chunked = []
  while start < len(arr):
    end = start + size
    chunked.append(arr[start:end])
    start = end

  return chunked
  