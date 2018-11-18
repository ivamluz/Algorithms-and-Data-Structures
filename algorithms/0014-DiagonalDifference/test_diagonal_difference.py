import unittest
from matrix import diagonal_difference

class TestDiagonalDifference(unittest.TestCase):
  def test_none_value(self):
    self.assertEquals(diagonal_difference(None), 0)

  def test_empty_matrix(self):
    self.assertEquals(diagonal_difference([]), 0)

if __name__ == '__main__':
  unittest.main()