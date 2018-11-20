import unittest
from matrix import min_max_sum

class TestMinMaxSum(unittest.TestCase):
  def test_none_value(self):
    self.assertEquals(min_max_sum(None), (0, 0))

  def test_empty_array(self):
    self.assertEquals(min_max_sum([]), (0, 0))

if __name__ == '__main__':
  unittest.main()