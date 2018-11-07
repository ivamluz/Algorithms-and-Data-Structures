def reverse_int(num):
  if num is None:
    return None

  sign = lambda x: (1, -1) [x < 0]

  abs_num = abs(num)
  reversed_num_str = str(abs_num)[::-1]
  reversed_num = int(reversed_num_str) * sign(num)

  return reversed_num