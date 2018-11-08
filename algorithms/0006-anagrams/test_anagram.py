import unittest
from anagram import is_anagram

class TestIsAnagram(unittest.TestCase):
  def test_both_strings_empty(self):
    self.assertFalse(is_anagram('', ''))

if __name__ == '__main__':
  unittest.main()