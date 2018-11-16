import unittest
from matrix import spiral

class TestSpiral(unittest.TestCase):
  def test_negative_size(self):
    with self.assertRaises(ValueError):
      spiral(-1)

  def test_zeroed_size(self):
    with self.assertRaises(ValueError):
      spiral(0)

  def test_single_sized_matrix(self):
    self.assertEquals(spiral(1), [[1]])

  def test_size_two_matrix(self):
    expected_output = [
      [1, 2],
      [4, 3]
    ]
    self.assertEquals(spiral(2), expected_output)

  def test_larger_matrix_even_size(self):
    expected_output = [
      [1,   2,  3, 4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10,  9,  8, 7]
    ]
    self.assertEquals(spiral(4), expected_output)

  def test_larger_matrix_odd_size(self):
    expected_output = [
      [1,   2,  3, 4,  5],
      [16, 17, 18, 19, 6],
      [15, 24, 25, 20, 7],
      [14, 23, 22, 21, 8],
      [13, 12, 11, 10, 9]
    ]
    self.assertEquals(spiral(5), expected_output)

if __name__ == '__main__':
  unittest.main()