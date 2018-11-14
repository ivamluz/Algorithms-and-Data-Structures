import unittest
from steps import steps

class TestSteps(unittest.TestCase):
  def test_negative_step_size(self):
    with self.assertRaises(ValueError):
      self.assertRaises(steps(-1))

  def test_zeroed_step_size(self):
    with self.assertRaises(ValueError):
      self.assertRaises(steps(0))

  def test_single_step(self):
    self.assertEquals(steps(1), "#")

  def test_multiple_steps(self):
    expected_output =  '#  \n'
    expected_output += '## \n'
    expected_output += '###'
    self.assertEquals(steps(3), expected_output)

if __name__ == '__main__':
  unittest.main()