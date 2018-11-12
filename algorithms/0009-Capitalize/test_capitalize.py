import unittest
from string_utils import capitalize

class TestCapitalize(unittest.TestCase):
  def test_none_string(self):
    self.assertEquals(capitalize(None), None)

  def test_empty_string(self):
    self.assertEquals(capitalize(''), '')

  def test_only_spaces(self):
    self.assertEquals(capitalize('   '), '   ')

  def test_only_numbers(self):
    self.assertEquals(capitalize('123'), '123')

  def test_single_string_uppercased(self):
    self.assertEquals(capitalize('ABC'), 'Abc')

  def test_multiple_strings_uppercased(self):
    self.assertEquals(capitalize('ABC DEF'), 'Abc Def')

  def test_single_string_lowercased(self):
    self.assertEquals(capitalize('abc'), 'Abc')

  def test_single_string_starting_with_numbers(self):
    self.assertEquals(capitalize('123abc'), '123abc')

  def test_single_string_starting_with_letters_containing_numbers(self):
    self.assertEquals(capitalize('abc123'), 'Abc123')

  def test_multiple_strings_starting_with_letters_containing_numbers(self):
    self.assertEquals(capitalize('abc123 def456'), 'Abc123 Def456')

  def test_multiple_strings_starting_with_letters_containing_numbers_and_vice_versa(self):
    self.assertEquals(capitalize('abc123 456def'), 'Abc123 456def')

  def test_multiple_spaces(self):
    self.assertEquals(capitalize('abc   def'), 'Abc   Def')

  def test_with_separators_other_than_spaces(self):
    self.assertEquals(capitalize(u'hello, how are you? i am fine!'), u'Hello, How Are You? I Am Fine!')

  def test_should_lower_case_non_first_chars(self):
    self.assertEquals(capitalize(u'hEllo, hOw aRe you? i am fine!'), u'Hello, How Are You? I Am Fine!')

if __name__ == '__main__':
  unittest.main()