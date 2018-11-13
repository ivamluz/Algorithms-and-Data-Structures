import unittest
from steps import steps

class TestSteps(unittest.TestCase):
  def test_negative_step_size(self):
    with self.assertRaises(ValueError):
      self.assertRaises(steps(-1))

  def test_zeroed_step_size(self):
    with self.assertRaises(ValueError):
      self.assertRaises(steps(0))

if __name__ == '__main__':
  unittest.main()