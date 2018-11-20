import unittest
from matrix import min_max_sum

class TestMinMaxSum(unittest.TestCase):
  INT32_MAX_VALUE = (2 ** 32) - 1

  def test_none_value(self):
    self.assertEquals(min_max_sum(None), (0, 0))

  def test_empty_list(self):
    self.assertEquals(min_max_sum([]), (0, 0))

  def test_sum_sorted_list(self):
    self.assertEquals(min_max_sum([1, 2, 3, 4, 5]), (10, 14))

  def test_sum_unsorted_list(self):
    self.assertEquals(min_max_sum([3, 1, 5, 4, 2]), (10, 14))

  def test_min_is_32bit_max_is_64bit(self):
    expected_max = 2 + 3 + 4 + TestMinMaxSum.INT32_MAX_VALUE
    self.assertEquals(min_max_sum([1, 2, 3, 4, TestMinMaxSum.INT32_MAX_VALUE]), (10, expected_max))

  def test_both_sums_are_64bit(self):
    expected_min = 1 + 2 + 3 + TestMinMaxSum.INT32_MAX_VALUE
    expected_max = 2 + 3 + TestMinMaxSum.INT32_MAX_VALUE + (TestMinMaxSum.INT32_MAX_VALUE + 1)
    self.assertEquals(min_max_sum([1, 2, 3, TestMinMaxSum.INT32_MAX_VALUE, TestMinMaxSum.INT32_MAX_VALUE + 1]), (expected_min, expected_max))

if __name__ == '__main__':
  unittest.main()