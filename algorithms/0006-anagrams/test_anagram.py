import unittest
from anagram import is_anagram

class TestIsAnagram(unittest.TestCase):
  def test_both_strings_empty(self):
    self.assertFalse(is_anagram('', ''))

  def test_first_string_empty(self):
    self.assertFalse(is_anagram('', 'earth'))

  def test_second_string_empty(self):
    self.assertFalse(is_anagram('earth', ''))

  def test_both_strings_none(self):
    self.assertFalse(is_anagram(None, None))

  def test_first_string_none(self):
    self.assertFalse(is_anagram(None, 'earth'))

  def test_second_string_none(self):
    self.assertFalse(is_anagram('earth', None))

if __name__ == '__main__':
  unittest.main()