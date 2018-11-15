import unittest
from matrix import spiral

class TestSpiral(unittest.TestCase):
  def test_negative_size(self):
    spiral(-1)

  def test_zeroed_size(self):
    spiral(0)

if __name__ == '__main__':
  unittest.main()