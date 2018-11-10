import unittest
from char_utils import max_occurring_chars

class TestMaxOccurringChars(unittest.TestCase):
  def test_none_string(self):
    self.assertIsNone(max_occurring_chars(None))

  def test_empty_string(self):
    self.assertIsNone(max_occurring_chars(''))

if __name__ == '__main__':
  unittest.main()