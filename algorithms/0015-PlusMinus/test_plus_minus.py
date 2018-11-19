import unittest
from matrix import plus_minus

class TestPlusMinus(unittest.TestCase):
  def test_none_value(self):
    self.assertEquals(plus_minus(None), [0, 0, 0])

  def test_empty_array(self):
    self.assertEquals(plus_minus([]), [0, 0, 0])

if __name__ == '__main__':
  unittest.main()