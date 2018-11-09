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

  def test_different_length_strings(self):
    self.assertFalse(is_anagram('area', 'era'))

  def test_same_string_same_case(self):
    self.assertTrue(is_anagram('area', 'area'))

  def test_same_string_different_case(self):
    self.assertTrue(is_anagram('AREA', 'area'))

  def test_different_strings_anagram(self):
    self.assertTrue(is_anagram('Earth', 'Heart'))

  def test_different_strings_same_size_non_anagram(self):
    self.assertFalse(is_anagram('Earth', 'Heard'))

if __name__ == '__main__':
  unittest.main()