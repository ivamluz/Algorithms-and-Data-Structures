from string_utils import count_vowels
import unittest

class TestCountVowels(unittest.TestCase):
  def test_none_value(self):
    self.assertEquals(count_vowels(None), 0)

  def test_empty_value(self):
    self.assertEquals(count_vowels(''), 0)

  def test_string_without_vowels(self):
    self.assertEquals(count_vowels('bcDfG'), 0)

  def test_string_with_lowercased_vowels(self):
    self.assertEquals(count_vowels('abcde'), 2)

  def test_string_with_uppercased_vowels(self):
    self.assertEquals(count_vowels('AbcdE'), 2)

  def test_string_with_mixed_case_vowels(self):
    self.assertEquals(count_vowels('Abcde'), 2)

  def test_should_count_more_than_one_occurrence(self):
    self.assertEquals(count_vowels('A man watches a Bird.'), 6)

if __name__ == '__main__':
  unittest.main()